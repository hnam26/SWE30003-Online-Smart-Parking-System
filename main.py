from BusinessLogic.bookingServices import BookingServices
from DataAccessLayer.models.personal.user import User
from BusinessLogic.userServices import UserServices
from BusinessLogic.parkingServices import ParkingServices
from DataAccessLayer.models.report.reportFactory import ReportFactory


def initialMenu():
    print("Please Log-in to continue")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice


def functionsMenu(user: User):
    reports = ReportFactory()
    name = user.getFirstName()
    print("Hello, " + name + "!")
    parkingServices = ParkingServices()
    userServices = UserServices()
    bookingServices = BookingServices()

    while True:
        print("What can we help you?")
        print("1. See All Available Parking Slots")
        print("2. Make Booking")
        print("3. Check In")
        print("4. Check Out")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                while True:
                    parkingServices.viewAvailableParkingSlots()
                    break
            case "2":
                while True:
                    slotNumber = input("Parking Slot: ")
                    parkingSlot = parkingServices.getParkingSlotByNumber(slotNumber)
                    if not parkingSlot:
                        print("Invalid Parking Slot Number\n")
                        continue

                    try:
                        duration = int(input("Duration: "))
                    except ValueError:
                        print("Invalid Duration. Please enter a number.\n")
                        continue

                    booking = userServices.makeBooking(user, parkingSlot, duration)
                    if booking:
                        print("Booking Successfully \n")
                        break
                    else:
                        print("Booking Failed\n")
                        break
            case "3":
                bookingId = input("Please enter your booking ID: ")
                # query the booking with the Id
                # booking ...
                # hay là kiếm cái booking mới nhất trong list user.getBooking()? (đoạn ni tùy logic e nha Sinh)
                if not bookingServices.checkIn(booking):
                    print("Check In Failed\n")
                    break

                print("Check In Successful\n")
                break
            case "4":
                bookingId = input("Please enter your booking ID: ")
                # query the booking with the id
                # booking ...
                # dưới ni cũng v

                if not bookingServices.checkOut(booking, user.getPayment()):
                    print("Check Out Failed\n")
                    break

                print("Check Out Successful\n")
                break
            case "5":
                while True:
                    reports.reportMenu()
                    break
            case "6":
                print("Thank You")
                break
            case _:
                print("Invalid Choice")


def main():
    print("Welcome to Online Smart Parking System")

    while True:
        choice = initialMenu()

        match choice:
            case "1":
                userServices = UserServices()
                while True:
                    user = userServices.login(input("Username: "), input("Password: "))
                    if user:
                        print("Login Successful!\n")
                        functionsMenu(user)
                        break
                    else:
                        print("Invalid Username or Password\n")
                        break
            case "2":
                userServices = UserServices()
                while True:
                    newUser = userServices.register(
                        input("First Name: "), input("Last Name: "), input("Email: "),
                        input("Phone Number: "), input("Date of Birth: "),
                        input("Username: "), input("Password: "))
                    
                    if not newUser:
                        print("Registration Failed\n")
                        break

                    print("Register Successful\n")
                    break
            case "3":
                print("Thank you for using Online Smart Parking System")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()
