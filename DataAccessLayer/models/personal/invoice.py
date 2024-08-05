from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from DataAccessLayer.models.base import Base
from typing import TYPE_CHECKING
from DataAccessLayer.models.payment.payment import Payment
class Invoice(Base):
    __tablename__ = 'Invoice'
    __invoiceId = Column("invoice_id", Integer, primary_key=True, autoincrement=True)
    __paymentId = Column("payment_id", Integer, ForeignKey('Payment.payment_id'), nullable=False, unique=True)
    __issueDate = Column("issue_date", DateTime, nullable=False)
    __amount = Column("amount", DECIMAL(10, 2), nullable=False)
    __payment = relationship('Payment', back_populates='invoice')

    @property
    def getAmount(self):
        return self.__amount

    @property
    def getPayment(self):
        return self.__payment
