from abc import ABC, abstractmethod
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from DataAccessLayer.personal.invoice import Invoice

Base = declarative_base()


class PaymentTable(Base):
    __tablename__ = 'Payment'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('Booking.booking_id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    payment_method = Column(String(50), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    user = relationship('UserTable', back_populates='payments')
    booking = relationship('BookingTable', back_populates='payment')
    invoice = relationship('InvoiceTable', uselist=False, back_populates='payment')


class Payment(ABC):
    def __init__(self, amount: int):
        self.__amount = amount
        self.__invoice = Invoice(self)

    @abstractmethod
    def processPayment(self, booking, amount) -> bool:
        """
    This method is intended to be implemented by subclasses to handle specific payment processing logic.
    It should attempt to process the payment for the provided Booking object and amount,
    returning True on success and False on failure.
    """
        pass

    def getAmount(self) -> float:
        return self.__amount

    def getInvoice(self) -> 'Invoice':
        return self.__invoice
