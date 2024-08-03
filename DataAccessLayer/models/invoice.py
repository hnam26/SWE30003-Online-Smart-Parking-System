from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .payment import Payment


class Invoice(Base):
    __tablename__ = 'Invoice'
    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey('Payment.payment_id'), nullable=False, unique=True)
    issue_date = Column(DateTime, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment = relationship('Payment', back_populates='invoice')