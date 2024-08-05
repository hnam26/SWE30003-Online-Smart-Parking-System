from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.parking.parkingSlot import ParkingSlot 
from DataAccessLayer.models.parking.parkingLot import ParkingLot 
from typing import Union


class ParkingServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.__session = self.__db.getSession()
        self.parkingLots = self.__session.query(ParkingLot).all()

    def getSession(self):
        return self.__db.getSession()

    def viewAllParkingLot(self):
        parkingLotsLocations = [parkingLot.getLocation for parkingLot in self.parkingLots]
        return parkingLotsLocations

    def viewAvailableParkingSlots(self, parkingLotLocation):
        for parkingLot in self.parkingLots:
            if parkingLot.getLocation == parkingLotLocation:
                break
        
        return parkingLot.getAllSlots


    def getParkingSlotByNumber(self, slotNumber: str) -> Union[ParkingSlot, None]:
        for parkingLot in self.parkingLots:
            parkingSlots = parkingLot.getAllSlots
            for parkingSlot in parkingSlots:
                if parkingSlot.getSlotNumber == slotNumber:
                    break
           
        return parkingSlot