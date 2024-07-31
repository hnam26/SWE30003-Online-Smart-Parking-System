from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.user.booking import Booking
from DataAccessLayer.user.user import User
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from BusinessLogic.bookingServices import BookingServices


class UserServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    def save(self):
        session = self.__db.getSession()
        try:
            session.add(self)
            session.commit()
            print("User record saved to the database.")
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

    def register(self):
        session = self.__db.getSession()
        try:
            firstName = input("Enter your first name: ")
            lastName = input("Enter your last name: ")
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            dob = input("Enter your date of birth: ")
            password = input("Enter your password: ")

            newUser = User(firstName=firstName, lastName=lastName, username=username, email=email, phone=phone, dob=dob,
                           password=password)
            session.add(newUser)
            session.commit()
            print("User registered successfully!")
            self.save()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()

    def login(self, username: str, password: str) -> bool:
        session = self.__db.getSession()
        user = session.query(User).filter_by(username=username, password=password).first()
        session.close()
        return user is not None

    def logout(self):
        return self.__db.logout()

    def makeBooking(self, user: User, parkingSlot: ParkingSlot, duration: int) -> [Booking, bool]:
        if not parkingSlot.getIsAvailable():
            return False

        booking = Booking(user, duration, parkingSlot)
        bookingServices = BookingServices()
        bookingServices.makePayment(booking, user.getPaymentMethod())
        if booking.isPaymentSuccessful():
            user.addBooking(booking)
            # add Booking record to db
            return booking
        return False
