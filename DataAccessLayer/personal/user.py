import re
from datetime import datetime
from typing import List, Union, TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking
    from .vehicle import Vehicle
    from DataAccessLayer.payment.payment import Payment


class User:
    def __init__(self, username: str, password: str, firstName: str, lastName: str, email: str, phone: str, dob: str,
                 vehicle: List['Vehicle'] = None, booking: List[Union['Booking', None]] = None,
                 payment: 'Payment' = None):
        self.__username = username
        self.__password = password
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = self.validateEmail(email)
        self.__phone = self.validatePhone(phone)
        self.__dob = self.validateDob(dob)
        self.__vehicle = vehicle
        self.__booking = booking
        self.__payment = payment

    @staticmethod
    def validateEmail(email: str) -> str:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address")
        return email

    @staticmethod
    def validatePhone(phone: str) -> str:
        phone_regex = r'^\d{10}$'
        if not re.match(phone_regex, phone):
            raise ValueError("Invalid phone number")
        return phone

    @staticmethod
    def validateDob(dob: str) -> str:
        dob_regex = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$'
        if not re.match(dob_regex, dob.strip()):
            raise ValueError("Invalid date of birth")
        date = datetime.strptime(dob, "%d-%m-%Y").date()
        return date.strftime("%Y-%m-%d")

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username: str):
        self.__username = username

    def getPassword(self) -> str:
        return self.__password

    def setPassword(self, password: str):
        self.__password = password

    def getFirstName(self) -> str:
        return self.__firstName

    def setFirstName(self, firstName: str):
        self.__firstName = firstName

    def getLastName(self) -> str:
        return self.__lastName

    def setLastName(self, lastName: str):
        self.__lastName = lastName

    def getFullName(self) -> str:
        return f"{self.__firstName} {self.__lastName}"

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email: str):
        self.__email = self.validateEmail(email)

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone: str):
        self.__phone = self.validatePhone(phone)

    def getDob(self) -> str:
        return self.__dob

    def setDob(self, dob: str):
        self.__dob = self.validateDob(dob)

    def getVehicles(self) -> List['Vehicle']:
        return self.__vehicle

    def addVehicle(self, vehicle: 'Vehicle'):
        self.__vehicle.append(vehicle)

    def getBookings(self) -> List[Union['Booking', None]]:
        return self.__booking

    def addBooking(self, booking: 'Booking'):
        self.__booking.append(booking)

    def getPaymentMethod(self) -> 'Payment':
        return self.__payment
