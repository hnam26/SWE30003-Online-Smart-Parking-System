from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class ParkingSlotTable(Base):
    __tablename__ = 'ParkingSlot'
    parking_slot_id = Column(Integer, primary_key=True, autoincrement=True)
    parking_lot_id = Column(Integer, ForeignKey('ParkingLot.parking_lot_id'), nullable=False)
    slot_number = Column(String(10), nullable=False)
    is_available = Column(Boolean, nullable=False)
    parking_lot = relationship('ParkingLotTable', back_populates='slots')
    bookings = relationship('BookingTable', back_populates='parking_slot')


class ParkingSlot:
    def __init__(self, location: str, isAvailable: bool):
        self.__location = location
        self.__isAvailable = isAvailable

    def getLocation(self) -> str:
        return self.__location
    
    def setLocation(self, location: str):
        self.__location = location

    def getIsAvailable(self) -> bool:
        return self.__isAvailable
    
    def setIsAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable

        