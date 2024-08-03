from DataAccessLayer.parking.parkingSlot import ParkingSlot
from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from sqlalchemy.orm import relationship, declarative_base
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .user import User


Base = declarative_base()


class BookingTable(Base):
    __tablename__ = 'Booking'
    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('Vehicle.vehicle_id'), nullable=False)
    parking_slot_id = Column(Integer, ForeignKey('ParkingSlot.parking_slot_id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    duration = Column(DECIMAL(2, 1), nullable=False)
    user = relationship('UserTable', back_populates='bookings')
    vehicle = relationship('VehicleTable', back_populates='bookings')
    parking_slot = relationship('ParkingSlotTable', back_populates='bookings')
    payment = relationship('PaymentTable', uselist=False, back_populates='booking')


class Booking:
    def __init__(self, user: 'User', duration: int, parkingSlot: ParkingSlot):
        self.__isLateCheckOut = False
        self.__user = user
        self.__duration = duration
        self.__parkingSlot = parkingSlot
        self.__isPaymentSuccessful = False
        self.__isCheckInSuccessful = False

    def getUser(self) -> 'User':
        return self.__user
    
    def getDuration(self) -> int:
        return self.__duration
    
    def getParkingSlot(self) -> ParkingSlot:
        return self.__parkingSlot

    def isPaymentSuccessful(self) -> bool:
        return self.__isPaymentSuccessful

    def setPaymentStatus(self, status: bool) -> None:
        self.__isPaymentSuccessful = status

    def isCheckInSuccessful(self) -> bool:
        return self.__isCheckInSuccessful

    def setCheckInStatus(self, status: bool) -> None:
        self.__isCheckInSuccessful = status
    
    def isLateCheckOut(self) -> bool:
        return self.__isLateCheckOut

    def setLateCheckOut(self, status: bool) -> None:
        self.__isLateCheckOut = status
