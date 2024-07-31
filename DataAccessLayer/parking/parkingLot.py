from parkingSlot import ParkingSlot
from typing import List
from DataAccessLayer.database.databaseAccess import DatabaseAccess


class ParkingLot:
    def __init__(self, name: str, slots: List[ParkingSlot], location: str, database: DatabaseAccess):
        self.__name = name
        self.__slots = slots
        self.__location = location
        self.__database = database
        # save new record to db

    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str):
        self.__name = name

    def getAllSlots(self) -> List[ParkingSlot]:
        return self.__slots
    
    def addSlot(self, slot: ParkingSlot):
        self.__slots.append(slot)

    def getLocation(self) -> str:
        return self.__location
    
    def setLocation(self, location: str):
        self.__location = location

