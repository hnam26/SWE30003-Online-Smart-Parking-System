from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .booking import Booking
    from .user import User
    from .invoice import Invoice

Base = declarative_base()


class Payment(Base):
    __tablename__ = 'Payment'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('Booking.booking_id'), nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    payment_method = Column(String(50), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='payments')
    booking = relationship('Booking', back_populates='payment')
    invoice = relationship('Invoice', uselist=False, back_populates='payment')