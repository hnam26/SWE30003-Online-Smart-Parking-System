# from sqlalchemy.ext.declarative import declarative_base
from abc import ABC, ABCMeta, abstractmethod
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.sql import expression
from ..base import Base

from ..personal.booking import Booking
from ..personal.user import User
from ..personal.invoice import Invoice


class Payment(Base):
    __tablename__ = 'Payment'
    __paymentId = Column("payment_id", Integer, primary_key=True, autoincrement=True)
    __bookingId = Column("booking_id", Integer, ForeignKey('Booking.booking_id'), nullable=False, unique=True)
    __userId = Column("user_id", Integer, ForeignKey('User.user_id'), nullable=False)
    __paymentMethod = Column("payment_method", String(50), nullable=False)
    __amount = Column("amount", DECIMAL(10, 2), nullable=False)
    __paymentDate = Column("payment_date", DateTime, nullable=False)

    user = relationship('User', back_populates='payments')
    booking = relationship('Booking', back_populates='payment')
    invoice = relationship('Invoice', uselist=False, back_populates='payment')

    # Constraint to restrict payment_method values
    __table_args__ = (
        CheckConstraint(
            expression.literal_column("payment_method").in_(['Visa', 'Master']),
            name='check_payment_method'
        ),
    )

    def __init__(self, paymentMethod: str, amount: float, booking: Booking):
        self.__paymentMethod = paymentMethod
        self.__amount = amount
        self.__booking = booking
    

    @abstractmethod
    def processPayment(self, booking: Booking, fee: float):
        return True
        pass

    @property
    def getAmount(self):
        return self.__amount

    @property
    def getInvoice(self):
        return self.invoice

    @property
    def getUser(self):
        return self.user

    @property
    def getPaymentMethod(self):
        return self.__paymentMethod

    @property
    def getPaymentDate(self):
        return self.__paymentDate

    @property
    def getBooking(self):
        return self.__booking
