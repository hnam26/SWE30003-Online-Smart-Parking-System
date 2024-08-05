class ParkingSlot:
    def __init__(self, parkingLotId: int, slotNumber: str, isAvailable: bool):
        self.__parkingLotId = parkingLotId
        self.__slotNumber = slotNumber
        self.__isAvailable = isAvailable

    def getParkingLotId(self) -> int:
        return self.__parkingLotId

    def getSlotNumber(self) -> str:
        return self.__slotNumber

    def setSlotNumber(self, value: str):
        self.__slotNumber = value

    def getIsAvailable(self) -> bool:
        return self.__isAvailable
    
    def setIsAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable

        