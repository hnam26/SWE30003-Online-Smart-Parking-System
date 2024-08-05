from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL, Enum
from sqlalchemy.orm import relationship
from ..base import Base
from enum import Enum as pythonEnum
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User
    from ..payment.payment import Payment
    from .vehicle import Vehicle
    from ..parking.parkingSlot import ParkingSlot
    
class BookingStatus(pythonEnum):
    PENDING = 'PENDING'
    PAID = 'PAID'
    IN = 'IN'
    OUT = 'OUT'
    CANCELLED = 'CANCELLED'

class Booking(Base):
    __tablename__ = 'Booking'
    __bookingId = Column("booking_id", Integer, primary_key=True, autoincrement=True)
    __userId = Column("user_id", Integer, ForeignKey('User.user_id'), nullable=False)
    __vehicleId = Column("vehicle_id", Integer, ForeignKey('Vehicle.vehicle_id'), nullable=False)
    __parkingSlotId = Column("parking_slot_id", Integer, ForeignKey('ParkingSlot.parking_slot_id'), nullable=False)
    __startTime = Column("start_time", DateTime, nullable=False)
    __duration = Column("duration", DECIMAL(2, 1), nullable=False)
    status = Column("status", Enum('PENDING', 'PAID', 'IN', 'OUT', 'CANCELLED'), nullable=False)

    user = relationship('User', back_populates='bookings')
    vehicle = relationship('Vehicle', back_populates='bookings')
    parkingSlot = relationship('ParkingSlot', back_populates='bookings')
    payment = relationship('Payment', uselist=False, back_populates='booking')


    @property
    def getUser(self):
        return self.user

    @property
    def getVehicle(self):
        return self.vehicle

    @property
    def getParkingSlotId(self):
        return self.__parkingSlotId

    @property
    def getStartTime(self):
        return self.__startTime

    @property
    def getDuration(self):
        return self.__duration

    @property
    def getStatus(self):
        return self.status

    @getStatus.setter
    def setStatus(self, status: BookingStatus):
        self.status = status

    @property
    def getBookingId(self):
        return self.__bookingId