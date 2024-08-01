from DataAccessLayer.utils.typesOfVehicle import TypesOfVehicle


class Vehicle:
    def __init__(self, licensePlate: str, vehicleType: TypesOfVehicle):
        self.__license = licensePlate
        self.__vehicleType = vehicleType

    def getLicensePlate(self) -> str:
        return self.__license
    
    def setLicensePlate(self, licensePlate: str):
        self.__license = licensePlate
    
    def getVehicleType(self) -> str:
        return self.__vehicleType.name
    
    def setVehicleType(self, vehicleType: TypesOfVehicle):
        self.__vehicleType = vehicleType
