from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.user import User
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal import user
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from BusinessLogic.bookingServices import BookingServices
from DataAccessLayer.database import models
from typing import Union

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
                validatedUser = User(
                    firstName=firstName,
                    lastName=lastName,
                    username=username,
                    email=email,
                    phone=phoneNumber,
                    dob=dob,
                    password=password
                )
                newUser = models.User(
                    first_name=validatedUser.getFirstName(),
                    last_name=validatedUser.getLastName(),
                    username=validatedUser.getUsername(),
                    email=validatedUser.getEmail(),
                    phone=validatedUser.getPhone(),
                    dob=validatedUser.getDob(),
                    password=validatedUser.getPassword()
                )
                session.add(newUser)
                session.commit()
                print("User registered successfully!")
                return newUser
            except Exception as e:
                session.rollback()
                print(f"An error occurred: {e}")
                retry = input("Would you like to try again? (y/n): ").strip().lower()
                if retry != 'y':
                    print("Exiting registration.")
                    return None
            finally:
                session.close()

    
    def login(self, username: str, password: str) -> Union[User, bool]:
        session = self.__db.getSession()
        user = session.query(models.User).filter_by(username=username, password=password).first()
        session.close()
        return user or False

    def logout(self):
        return self.__db.logout()

    def getParkingSlotByNumber(self, slot_number: str) -> Union[ParkingSlot, None]:
        session = self.__db.getSession()
        try:
            parking_slot = session.query(models.ParkingSlot).filter_by(slot_number=slot_number).first()
            return parking_slot
        except Exception as e:
            print(f"An error occurred while fetching the parking slot: {e}")
            return None
        finally:
            session.close()

    def makeBooking(self, user: user.User, parkingSlot: ParkingSlot, duration: int) -> Union[Booking, False]:
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
