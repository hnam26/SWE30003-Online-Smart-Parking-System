from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from DataAccessLayer.payment.payment import Payment

Base = declarative_base()


class InvoiceTable(Base):
    __tablename__ = 'Invoice'
    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey('Payment.payment_id'), nullable=False, unique=True)
    issue_date = Column(DateTime, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment = relationship('PaymentTable', back_populates='invoice')


class Invoice:
    def __init__(self, payment: 'Payment'):
        self.__payment = payment
        self.__amount = payment.getAmount()

    def getAmount(self) -> float:
        return self.__amount

    def getPayment(self) -> 'Payment':
        return self.__payment
