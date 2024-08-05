from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship
from DataAccessLayer.models.base import Base
from typing import TYPE_CHECKING
from DataAccessLayer.models.user import User

class Booking(Base):
    __tablename__ = 'Booking'
    __bookingId = Column("booking_id", Integer, primary_key=True, autoincrement=True)
    __userId = Column("user_id", Integer, ForeignKey('User.user_id'), nullable=False)
    __vehicleId = Column("vehicle_id", Integer, ForeignKey('Vehicle.vehicle_id'), nullable=False)
    __parkingSlotId = Column("parking_slot_id", Integer, ForeignKey('ParkingSlot.parking_slot_id'), nullable=False)
    __startTime = Column("start_time", DateTime, nullable=False)
    __duration = Column("duration", DECIMAL(2, 1), nullable=False)

    __user = relationship('User', back_populates='bookings')
    __vehicle = relationship('Vehicle', back_populates='bookings')
    __parkingSlot = relationship('ParkingSlot', back_populates='bookings')
    __payment = relationship('Payment', uselist=False, back_populates='booking')

    @property
    def getUser(self):
        return self.__user

    @property
    def getVehicle(self):
        return self.__vehicle

    @property
    def getParkingSlot(self):
        return self.__parkingSlot

    @property
    def getStartTime(self):
        return self.__startTime

    @property
    def getDuration(self):
        return self.__duration
