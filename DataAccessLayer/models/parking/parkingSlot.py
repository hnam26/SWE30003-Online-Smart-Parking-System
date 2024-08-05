from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from DataAccessLayer.models.base import Base


class ParkingSlot(Base):
    __tablename__ = 'ParkingSlot'
    __parkingSlotId = Column("parking_slot_id", Integer, primary_key=True, autoincrement=True)
    __parkingLotId = Column("parking_lot_id", Integer, ForeignKey('ParkingLot.parking_lot_id'), nullable=False)
    __slotNumber = Column("slot_number", String(10), nullable=False)
    __isAvailable = Column("is_available", Boolean, nullable=False)
    __parkingLot = relationship('ParkingLot', back_populates='slots')
    __bookings = relationship('Booking', back_populates='parking_slot')

    @property
    def getSlotNumber(self):
        return self.__slotNumber

    @property
    def getIsAvailable(self):
        return self.__isAvailable

    @getIsAvailable.setter
    def setIsAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable
