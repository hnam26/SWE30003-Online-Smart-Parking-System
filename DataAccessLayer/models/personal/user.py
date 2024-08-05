import re
from sqlalchemy import Column, Integer, String, Date, CheckConstraint
from sqlalchemy.orm import relationship
from ..base import Base
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

    vehicles = relationship('Vehicle', back_populates='user')
    bookings = relationship('Booking', back_populates='user')
    payments = relationship('Payment', back_populates='user')

    __table_args__ = (
        CheckConstraint(
            'email ~* \'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$\'',
            name='check_email_format'
        ),
        CheckConstraint(
            'phone ~* \'^\d{10}$\'',
            name='check_phone_format'
        ),
        CheckConstraint(
            'dob <= CURRENT_DATE',
            name='check_dob_past'
        ),
    )

    def __init__(self, email, phone, dob, username, password, firstName, lastName):
        self.__email = self.validateEmail(email)
        self.__phone = self.validatePhone(phone)
        self.__dob = self.validateDob(dob)
        self.__username = username
        self.__password = password
        self.__firstName = firstName
        self.__lastName = lastName


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
        dob_str = str(dob).strip()
        if not re.match(dob_regex, dob_str):
            raise ValueError("Invalid date of birth")
        date = datetime.strptime(dob, "%d-%m-%Y").date()
        return date
    
    @property
    def getVehicle(self):
        return self.vehicles

    @property
    def getBookings(self):
        return self.bookings

    @property
    def getPayment(self):
        return self.payments

    @property
    def getUsername(self):
        return self.__username

    @property
    def getPassword(self):
        return self.__password
    
    @property
    def getFirstName(self):
        return self.__firstName
    
    @property
    def getLastName(self):
        return self.__lastName
    
    @property
    def getEmail(self):
        return self.__email
    
    @property
    def getPhone(self):
        return self.__phone
    
    @property
    def getDob(self):
        return self.__dob

    @property
    def getUserId(self):
        return self.__userId