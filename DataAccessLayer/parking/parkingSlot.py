class ParkingSlot:
    def __init__(self, location: str):
        self.__location = location
        self.__isAvailable = True

    def getLocation(self) -> str:
        return self.__location
    
    def setLocation(self, location: str):
        self.__location = location

    def getIsAvailable(self) -> bool:
        return self.__isAvailable
    
    def setIsAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable

        