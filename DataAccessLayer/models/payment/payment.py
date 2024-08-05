from abc import ABC, abstractmethod

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CheckConstraint
from sqlalchemy.sql import expression

from DataAccessLayer.models.base import Base
from DataAccessLayer.models.personal.booking import Booking
from DataAccessLayer.models.personal.user import User
from DataAccessLayer.models.personal.invoice import Invoice


class Payment(Base, ABC):
    __tablename__ = 'Payment'
    __paymentId = Column("payment_id", Integer, primary_key=True, autoincrement=True)
    __bookingId = Column("booking_id", Integer, ForeignKey('Booking.booking_id'), nullable=False, unique=True)
    __userId = Column("user_id", Integer, ForeignKey('User.user_id'), nullable=False)
    __paymentMethod = Column("payment_method", String(50), nullable=False)
    __amount = Column("amount", DECIMAL(10, 2), nullable=False)
    __paymentDate = Column("payment_date", DateTime, nullable=False)
    __user = relationship('User', back_populates='payments')
    __booking = relationship('Booking', back_populates='payment')
    __invoice = relationship('Invoice', uselist=False, back_populates='payment')

    # Constraint to restrict payment_method values
    __table_args__ = (
        CheckConstraint(
            expression.literal_column("payment_method").in_(['Visa', 'Master']),
            name='check_payment_method'
        ),
    )

    def __init__(self, paymentMethod: str, amount: float, booking: Booking, invoice: Invoice, user: User):
        super().__init__()
        self.__paymentMethod = paymentMethod
        self.__amount = amount
        self.__booking = booking
        self.__invoice = invoice
        self.__user = user

    @abstractmethod
    def processPayment(self, booking: Booking, fee: float):
        pass

    @property
    def getAmount(self):
        return self.__amount

    @property
    def getInvoice(self):
        return self.__invoice

    @property
    def getUser(self):
        return self.__user

    @property
    def getPaymentMethod(self):
        return self.__paymentMethod

    @property
    def getPaymentDate(self):
        return self.__paymentDate

    @property
    def getBooking(self):
        return self.__booking
