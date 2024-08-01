from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal.user import User
from DataAccessLayer.user.booking import Booking
from DataAccessLayer.user import user
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from BusinessLogic.bookingServices import BookingServices

from DataAccessLayer.database import models


class UserServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    def save(self, user: user.User):
        session = self.__db.getSession()
        try:
            user_item = models.User(
                username=user.getUsername(),
                password=user.getPassword(),
                first_name=user.getFirstName(),
                last_name=user.getLastName(),
                email=user.getEmail(),
                phone=user.getPhone(),
                dob=user.getDob()
            )
            session.add(user_item)
            session.commit()
            print("User registered successfully!")
            return False
        except Exception as e:
            session.rollback()
            # raise e
            print(f"An error occurred: {e}")
            retry = input("Would you like to try again? (y/n): ").strip().lower()
            return retry.lower() == 'y'
        finally:
            session.close()

    def register(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str, password: str):
        while True:
            # first_name = input("Enter your first name: ")
            # last_name = input("Enter your last name: ")
            # username = input("Enter your username: ")
            # email = input("Enter your email: ")
            # phone = input("Enter your phone number: ")
            # dob = input("Enter your date of birth: ")
            # password = input("Enter your password: ")

            # For testing purposes
            first_name = "Wendell"
            last_name = "Talman"
            username = "talman123"
            email = "wendelltalman@mail.net"
            phone = "0912345678"
            dob = "06-12-1998"
            password = "12312312"

            newUser = user.User(first_name=first_name, last_name=last_name, username=username, email=email, phone=phone, dob=dob, password=password)
            input(f"Created user object for {first_name}. Enter to continue")
            result = self.save(newUser)
            if not result:
                print("Exiting registration.")
                break
            session = self.__db.getSession()
            try:
                newUser = User(firstName=firstName, lastName=lastName, username=username, email=email, phone=phoneNumber,
                               dob=dob, password=password)
                session.add(newUser)
                session.commit()
                print("User registered successfully!")
                self.save(newUser)
            except Exception as e:
                session.rollback()
                print(f"An error occurred: {e}")
                retry = input("Would you like to try again? (y/n): ").strip().lower()
                if retry != 'y':
                    print("Exiting registration.")
                    break
            finally:
                session.close()

    def login(self, username: str, password: str) -> [User, False]:
        session = self.__db.getSession()
        user = session.query(models.User).filter_by(username=username, password=password).first()
        session.close()
        return user is not None

    def logout(self):
        return self.__db.logout()

    def makeBooking(self, user: user.User, parkingSlot: ParkingSlot, duration: int) -> [Booking, bool]:
        session = self.__db.getSession()
        try:
            if not parkingSlot.getIsAvailable():
                return False

            booking = Booking(user, duration, parkingSlot)
            bookingServices = BookingServices()
            bookingServices.makePayment(booking, user.getPaymentMethod())

            if booking.isPaymentSuccessful():
                session.add(booking)
                session.commit()
                print("Booking record saved to the database.")
                return booking, True
            else:
                return False
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            session.close()
