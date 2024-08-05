from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from .base import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking
    from .user import User
    from .invoice import Invoice



class Payment(Base):
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