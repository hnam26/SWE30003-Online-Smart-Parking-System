from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from DataAccessLayer.models.base import Base

class ParkingLot(Base):
    __tablename__ = 'ParkingLot'
    __parkingLotId = Column("parking_lot_id", Integer, primary_key=True, autoincrement=True)
    __name = Column("name", String(50), nullable=True)
    __location = Column("location", String(100), nullable=False)
    
    slots = relationship('ParkingSlot', back_populates='parkingLot')

    @property
    def getName(self) -> str:
        return self.__name

    @property
    def getLocation(self) -> str:
        return self.__location

    @property
    def getAllSlots(self) -> list:
        return self.slots

    @property
    def getParkingLotId(self):
        return self.__parkingLotId
