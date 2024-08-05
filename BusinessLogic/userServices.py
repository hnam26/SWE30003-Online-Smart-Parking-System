import bcrypt
from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.personal import Booking, vehicle as vehicleClass
from DataAccessLayer.models.personal.user import User
from DataAccessLayer.models.user import User as UserModel
from DataAccessLayer.models.parking import ParkingSlot
from DataAccessLayer.models.personal.vehicle import Vehicle
from DataAccessLayer.models.utils.typesOfVehicle import TypesOfVehicle
from BusinessLogic.bookingServices import BookingServices
from typing import Union


class UserServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.session = self.__db.getSession()

    def save(self):
        try:
            self.session.add(self)
            self.session.commit()
            print("User record saved to the database.")
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")
        finally:
            self.session.close()

    def getUserById(self, userId: int):
        try:
            return self.session.query(UserModel).filter(UserModel.user_id == userId).first()
        except Exception as e:
            print(f"An error occurred when trying to get user {userId}: {e}")
            return None
        finally:
            self.session.close()

    def responseUser(self, user: UserModel):
        return User(
            firstName=user.first_name,
            lastName=user.last_name,
            username=user.username,
            email=user.email,
            phone=user.phone,
            dob=user.dob.strftime("%d-%m-%Y"),
            password=user.password
        )

    def registerUser(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str,
                      password: str) -> Union[int, None]:
        try:
            validatedUser = User(
                firstName=firstName,
                lastName=lastName,
                username=username,
                email=email,
                phone=phoneNumber,
                dob=dob,
                password=bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )
            newUser = UserModel(
                first_name=validatedUser.getFirstName(),
                last_name=validatedUser.getLastName(),
                username=validatedUser.getUsername(),
                email=validatedUser.getEmail(),
                phone=validatedUser.getPhone(),
                dob=validatedUser.getDob(),
                password=validatedUser.getPassword()
            )
            self.session.add(newUser)
            self.session.commit()
            print("User registered successfully!")
            return newUser.user_id
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")
            return None
        finally:
            self.session.close()

        

    def registerVehicle(self, user_id: int, licensePlate: str, vehicleTypeStr: str) -> Union[Vehicle, None]:
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
            self.session.add(newVehicle)
            self.session.commit()
            print("Vehicle registered successfully!")
            return newVehicle
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")
            return None
        finally:
            self.session.close()

    def register(self, firstName: str, lastName: str, email: str, phoneNumber: str, dob: str, username: str,
                 password: str):
        while True:
            user_id = self.registerUser(firstName, lastName, email, phoneNumber, dob, username, password)
            if user_id is not None:
                print("Please register your vehicle")
                licensePlate = input("License Plate: ")
                vehicleTypeStr = input("Vehicle Type: ")
                newVehicle = self.registerVehicle(user_id, licensePlate, vehicleTypeStr)
                if newVehicle is not None:
                    return user_id, newVehicle
                else:
                    break
            else:
                break

    def login(self, username: str, password: str) -> Union[User, None]:
        # user = self.session.query(User).filter_by(username=username, password=password).first()
        # self.session.close()
        user = self.session.query(UserModel).filter(UserModel.username == username).first()
        if user is None:
            return None
        valid_password = bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))
        return self.responseUser(user) if valid_password else None
        # return user or False

    def logout(self):
        return self.__db.logout()


    def makeBooking(self, user: User, parkingSlot: ParkingSlot, duration: int) -> Union[Booking, False]:
        try:
            session = self.__db.getSession()
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
            raise e
            print(f"An error occurred: {e}")
            return False
        finally:
            session.close()
