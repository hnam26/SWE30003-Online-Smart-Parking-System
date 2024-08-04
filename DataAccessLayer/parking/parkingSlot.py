class ParkingSlot:
    def __init__(self, location: str, slot_number: str):
        self.__location = location
        # làm sao cho nó thống nhất vs bên table nhé
        self.__slot_number = slot_number
        self.__isAvailable = True

    def getLocation(self) -> str:
        return self.__location
    
    def setLocation(self, location: str):
        self.__location = location

    def getSlotNumber(self) -> str:
        return self.__slot_number

    def setSlotNumber(self, value: str):
        self.__slot_number = value

    def getIsAvailable(self) -> bool:
        return self.__isAvailable
    
    def setIsAvailable(self, isAvailable: bool):
        self.__isAvailable = isAvailable

        