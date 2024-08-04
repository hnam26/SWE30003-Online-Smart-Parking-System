from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal import user as userClass
from DataAccessLayer.models.user import User
from DataAccessLayer.models.booking import Booking as BookingModel
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from DataAccessLayer.personal import vehicle as vehicleClass
from DataAccessLayer.models.vehicle import Vehicle
from DataAccessLayer.utils.typesOfVehicle import TypesOfVehicle
from DataAccessLayer.models import parkingSlot as parkingSlotModel
from BusinessLogic.bookingServices import BookingServices
from typing import Union, List

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

    def register_user(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str,
                      password: str) -> Union[int, None]:
        session = self.__db.getSession()
        try:
            validatedUser = userClass.User(
                firstName=firstName,
                lastName=lastName,
                username=username,
                email=email,
                phone=phoneNumber,
                dob=dob,
                password=password
            )
            newUser = User(
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
            return newUser.user_id
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            return None
        finally:
            session.close()

    def register_vehicle(self, user_id: int, licensePlate: str, vehicleTypeStr: str) -> Union[Vehicle, None]:
        session = self.__db.getSession()
        try:
            try:
                vehicleType = TypesOfVehicle[vehicleTypeStr]
            except KeyError:
                print("Invalid vehicle type. Please try again.")
                return None

            vehicleInstance = vehicleClass.Vehicle(
                licensePlate=licensePlate,
                vehicleType=vehicleType
            )
            newVehicle = Vehicle(
                user_id=user_id,
                license_plate=vehicleInstance.getLicensePlate(),
                vehicle_type=vehicleInstance.getVehicleType()
            )
            session.add(newVehicle)
            session.commit()
            print("Vehicle registered successfully!")
            return newVehicle
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
            return None
        finally:
            session.close()

    def register(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str,
                 password: str):
        while True:
            user_id = self.register_user(firstName, lastName, email, phoneNumber, dob, username, password)
            if user_id is not None:
                print("Please register your vehicle")
                licensePlate = input("License Plate: ")
                vehicleTypeStr = input("Vehicle Type: ")
                newVehicle = self.register_vehicle(user_id, licensePlate, vehicleTypeStr)
                if newVehicle is not None:
                    return user_id, newVehicle
                else:
                    retry = input("Would you like to try again? (y/n): ").strip().lower()
                    if retry != 'y':
                        print("Exiting registration.")
                        return user_id, None
            else:
                retry = input("Would you like to try again? (y/n): ").strip().lower()
                if retry != 'y':
                    print("Exiting registration.")
                    return None, None

    
    def login(self, username: str, password: str) -> Union[User, bool]:
        session = self.__db.getSession()
        user = session.query(User).filter_by(username=username, password=password).first()
        session.close()
        return user or False

    def logout(self):
        return self.__db.logout()

    def getParkingSlotByNumber(self, slot_number: str) -> Union[ParkingSlot, None]:
        session = self.__db.getSession()
        try:
            parking_slot = session.query(parkingSlotModel.ParkingSlot).filter_by(slot_number=slot_number).first()
            return parking_slot
        except Exception as e:
            print(f"An error occurred while fetching the parking slot: {e}")
            return None
        finally:
            session.close()

    def makeBooking(self, user: userClass.User, parkingSlot: ParkingSlot, duration: int) -> Union[Booking, False]:
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
