import re
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime



class User(Base):
    __tablename__ = 'User'
    __userId = Column("user_id", Integer, primary_key=True, autoincrement=True)
    __username = Column("username", String(100), nullable=False)
    __password = Column("password", String(60), nullable=False)
    __firstName = Column("first_name", String(100), nullable=False)
    __lastName = Column("last_name", String(100), nullable=False)
    __email = Column("email", String(100), unique=True, nullable=False)
    __phone = Column("phone", String(10), nullable=False)
    __dob = Column("dob", Date, nullable=False)

    __vehicles = relationship('Vehicle', back_populates='user')
    __bookings = relationship('Booking', back_populates='user')
    __payments = relationship('Payment', back_populates='user')

    def __init__(self, email, phone, dob):
        self.__email = self.validateEmail(email)
        self.__phone = self.validatePhone(phone)
        self.__dob = self.validateDob(dob)

    @staticmethod
    def validateEmail(email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValueError("Invalid email address")
        return email

    @staticmethod
    def validatePhone(phone):
        phone_regex = r'^\d{10}$'
        if not re.match(phone_regex, phone):
            raise ValueError("Invalid phone number")
        return phone
    
    @staticmethod
    def validateDob(dob):
        dob_regex = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(\d{4})$'
        if not re.match(dob_regex, dob.strip()):
            raise ValueError("Invalid date of birth")
        date = datetime.strptime(dob, "%d-%m-%Y").date()
        return date
    
    @property
    def getVehicle(self):
        for __vehicle in self.__vehicles:
            return __vehicle
        
    @property
    def getBooking(self):
        for __booking in self.__bookings:
            return __booking
    
    @property
    def getPayment(self):
        for __payment in self.__payments:
            return __payment
        
    @property
    def getUsername(self):
        return self.__username
    
    @property
    def getPassword(self):
        return self.__password
    
    
