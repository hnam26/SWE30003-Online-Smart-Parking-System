import bcrypt
from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.personal.booking import Booking
from DataAccessLayer.models.personal.user import User
from DataAccessLayer.models.parking.parkingSlot import ParkingSlot
from DataAccessLayer.models.personal.vehicle import Vehicle
from DataAccessLayer.models.utils.typesOfVehicle import TypesOfVehicle
from BusinessLogic.bookingServices import BookingServices
from typing import Union


class UserServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.__session = self.__db.getSession()

    def save(self):
        try:
            self.__session.add(self)
            self.__session.commit()
            print("User record saved to the database.")
        except Exception as e:
            self.__session.rollback()
            print(f"An error occurred: {e}")
        finally:
            self.__session.close()

    def getUserById(self, userId: int):
        try:
            return self.__session.query(User).filter(User.user_id == userId).first()
        except Exception as e:
            print(f"An error occurred when trying to get user {userId}: {e}")
            return None
        finally:
            self.__session.close()

    def responseUser(self, user: User):
        return User(
            firstName=user.getFirstName,
            lastName=user.getLastName,
            username=user.getUsername,
            email=user.getEmail,
            phone=user.getPhone,
            dob=user.getDob.strftime("%d-%m-%Y"),
            password=user.getPassword
        )

    def registerUser(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str,
                      password: str) -> Union[int, None]:
        try:
            newUser = User(
                firstName=firstName,
                lastName=lastName,
                username=username,
                email=email,
                phone=phoneNumber,
                dob=dob,
                password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )

            self.__session.add(newUser)
            self.__session.commit()
            print("User registered successfully!")
            return newUser.getUserId
        except Exception as e:
            self.__session.rollback()
            print(f"An error occurred: {e}")
            return None
        finally:
            self.__session.close()

        

    def registerVehicle(self, userId: int, licensePlate: str, vehicleTypeStr: str) -> Union[Vehicle, None]:
        try:
            try:
                vehicleType = TypesOfVehicle[vehicleTypeStr]
            except KeyError:
                print("Invalid vehicle type. Please try again.")
                return None

            newVehicle = Vehicle(
                userId=userId,
                licensePlate=licensePlate,
                vehicleType=vehicleType
            )
            self.__session.add(newVehicle)
            self.__session.commit()
            print("Vehicle registered successfully!")
            return newVehicle
        except Exception as e:
            self.__session.rollback()
            print(f"An error occurred: {e}")
            return None
        finally:
            self.__session.close()

    def register(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str,
                 password: str):
        while True:
            userId = self.registerUser(firstName, lastName, email, phoneNumber, dob, username, password)
            if userId is not None:
                print("Please register your vehicle")
                licensePlate = input("License Plate: ")
                 # Display the available vehicle types
                print("Vehicle Types Available:")
                for vehicle_type in TypesOfVehicle:
                    print(f"{vehicle_type.name}")

                # Ask the user to select a vehicle type
                vehicleTypeStr = input("Please select a vehicle type from the above options: ")
                newVehicle = self.registerVehicle(userId, licensePlate, vehicleTypeStr)
                if newVehicle is not None:
                    return userId, newVehicle
                else:
                    break
            else:
                break

    def login(self, username: str, password: str) -> Union[User, None]:
        users = (self.__session.query(User).all())
        for user in users:
            if user.getUsername == username:
                break
        
        valid_password = bcrypt.checkpw(password.encode('utf-8'), user.getPassword.encode('utf-8'))
        print(valid_password)
        return self.responseUser(user) if valid_password else None


    def makeBooking(self, user: User, parkingSlot: ParkingSlot, duration: int) -> Union[Booking, False]:
        try:
            session = self.__db.getSession()
            if not parkingSlot.getIsAvailable:
                return False

            booking = Booking()
            bookingServices = BookingServices()
            

            if bookingServices.makePayment(booking, duration):
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
