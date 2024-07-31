import re
from typing import List
from booking import Booking
from parking.parkingSlot import ParkingSlot
from payment.payment import Payment
from vehicle import Vehicle

class User:
    def __init__(self, username: str, password: str, firstName: str, lastName: str, email: str, phone: str, dob: str, vehicle: List[Vehicle], booking: List[Booking, None], payment : Payment):
        self.__username = username
        self.__password = password
        self._firstName = firstName
        self._lastName = lastName
        self._email = self.validateEmail(email)
        self._phone = self.validatePhone(phone)
        self._dob = self.validateDob(dob) 
        self._vehicle = vehicle
        self._booking = booking
        self._payment = payment

    def validateEmail(self, email: str) -> str:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address")
        return email

    def validatePhone(self, phone: str) -> str:
        phone_regex = r'^\d{10}$'
        if not re.match(phone_regex, phone):
            raise ValueError("Invalid phone number")
        return phone

    def validateDob(self, dob: str) -> str:
        dob_regex = r'^(0[1-9]|[12][0-9]|3[01])-/.-/.\d\d$'
        if not re.match(dob_regex, dob):
            raise ValueError("Invalid date of birth")
        return dob

    def getUsername(self) -> str:
        return self.__username

    def setUsername(self, username: str):
        self.__username = username

    def getPassword(self) -> str:
        return self.__password
    
    def setPassword(self, password: str):
        self.__password = password

    def getFirstName(self) -> str:
        return self._firstName
    
    def setFirstName(self, firstName: str):
        self._firstName = firstName

    def getLastName(self) -> str:
        return self._lastName
    
    def setLastName(self, lastName: str):
        self._lastName = lastName

    def getFullName(self) -> str:
        return f"{self._firstName} {self._lastName}"
    
    def getEmail(self) -> str:
        return self._email
    
    def setEmail(self, email: str):
        self._email = self.validateEmail(email)

    def getPhone(self) -> str:
        return self._phone
    
    def setPhone(self, phone: str):
        self._phone = self.validatePhone(phone)

    def getDob(self) -> str:
        return self._dob
    
    def setDob(self, dob: str):
        self._dob = self.validateDob(dob)

    def getVehicles(self) -> List[Vehicle]:
        return self._vehicle
    
    def addVehicle(self, vehicle: Vehicle):
        self._vehicle.append(vehicle)

    def getBookings(self) -> List[Booking, None]:
        return self._booking
    
    def makeBooking(self, duration: int, parkingSlot: ParkingSlot) -> Booking:
        if not parkingSlot.getIsAvailable():
            return "Parking slot is not available"
        booking = Booking(duration, parkingSlot)       
        booking.makePayment(self._payment)
        if booking.isPaymentSuccessful():
            self._booking.append(booking)
            return booking
        return None

        
        
