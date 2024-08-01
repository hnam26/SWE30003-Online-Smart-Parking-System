import BusinessLogic
from BusinessLogic.bookingServices import BookingServices
from BusinessLogic.invoiceServices import InvoiceServices
from DataAccessLayer.personal.user import User
from BusinessLogic.userServices import UserServices


def initialMenu():
    print("Please Log-in to continue")
    print("1. Login")
    print("2. Register")
    print("3. Exit")

    choice = input("Enter your choice: ")
    return choice


def functionsMenu(user: User):
    print("What can we help you?")
    userServices = UserServices()
    bookingServices = BookingServices()
    invoiceServices = InvoiceServices()


def main():
    # Đây là 2 phần code của report để em test thử nó chạy được chưa,
    # khi mà mình có option để chọn print report thì có thể bỏ đoạn này vào.

    # Initialize the ReportFactory with the database connection
    # ReportFactory.initialize_database()
    #
    # # Run the report generation process
    # ReportFactory.run_report_generation()

    # Initialize DatabaseAccess
    # db_access = DatabaseAccess()
    #
    # # Create a session to interact with the database
    # session = db_access.getSession()
    # user_service = UserServices()
    # user_service.register()
    # # db_access.queryMenu()
    # # Close the session
    # session.close()
    print("Welcome to Online Smart Parking System")

    while True:
        choice = initialMenu()
        userServices = UserServices()

        if choice == "1":

            while True:
                user = userServices.login(input("Username: "), input("Password: "))
                if user:
                    print("Login Successful\n")
                    functionsMenu(user)
                    break
                else:
                    print("Invalid Username or Password\n")
                    break
        elif choice == "2":
            while True:
                newUser = userServices.register(input("First Name: "), input("Last Name: "), input("Email: "),
                                                input("Phone Number"), input("Date of Birth: "),
                                                input("Username: "), input("Password: "))

                if not newUser:
                    print("Registration Failed\n")
                    break

                print("Register Successful\n")
                break

        elif choice == "3":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
