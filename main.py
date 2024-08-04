import BusinessLogic
from BusinessLogic.bookingServices import BookingServices
from BusinessLogic.invoiceServices import InvoiceServices
from DataAccessLayer.personal.user import User
from BusinessLogic.userServices import UserServices
from BusinessLogic.parkingServices import ParkingServices
from DataAccessLayer.report.reportFactory import ReportFactory


def initialMenu():
    print("Please Log-in to continue")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice


def functionsMenu(user: User):
    while True:
        reports = ReportFactory()
        parkingServices = ParkingServices()
        userServices = UserServices()
        # bookingServices = BookingServices()
        # invoiceServices = InvoiceServices()
        print("What can we help you?")
        print("1. See All Available Parking Slots")
        print("2. Make Booking")
        print("3. Check In")
        print("4. Check Out")
        print("5. Generate Report")
        print("5. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                while True:
                    parkingServices.viewAvailableParkingSlots()
                    break
            case "2":
                while True:
                    slotNumber = input("Parking Slot: ")
                    parkingSlot = userServices.getParkingSlotByNumber(slotNumber)
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
                break
            case "4":
                break
            case "5":
                while True:
                    reports.reportMenu()
                    break
            case "6":
                print("Thank You")
                break
            case default:
                print("Invalid Choice")


def main():
    print("Welcome to Online Smart Parking System")

    while True:
        choice = initialMenu()
        userServices = UserServices()
        match choice:

            case "1":

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
                while True:
                    newUser = userServices.register(input("First Name: "), input("Last Name: "), input("Email: "),
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

            case default:
                print("Invalid choice")


if __name__ == "__main__":
    main()
