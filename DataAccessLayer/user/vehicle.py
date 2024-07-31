from DataAccessLayer.utils.typesOfVehicle import TypesOfVehicle

class Vehicle:
    def __init__(self, license : str, vehicleType : TypesOfVehicle):
        self.__license = license
        self.__vehicleType = vehicleType

    def __str__(self) -> str:
        return f"This is a car with:\nLicense: {self.getLicense()}\nType: {self.getVehicleType()}"

    def getLicense(self) -> str:
        return self.__license
    
    def setLicense(self, license: str):
        self.__license = license
    
    def getVehicleType(self) -> str:
        return self.__vehicleType.name
    
    def setVehicleType(self, vehicleType: TypesOfVehicle):
        self.__vehicleType = vehicleType
