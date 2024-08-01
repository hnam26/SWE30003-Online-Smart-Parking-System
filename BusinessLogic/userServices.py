from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal.user import User
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

    def register(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str, password: str):
        while True:
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
        user = session.query(User).filter_by(username=username, password=password).first()
        session.close()
        return user or False

    def makeBooking(self, user: User, parkingSlot: ParkingSlot, duration: int) -> [Booking, bool]:
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
