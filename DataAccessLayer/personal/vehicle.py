from DataAccessLayer.utils.typesOfVehicle import TypesOfVehicle
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class VehicleTable(Base):
    __tablename__ = 'Vehicle'
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    license_plate = Column(String(20), unique=True, nullable=False)
    vehicle_type = Column(String(50), nullable=False)
    user = relationship('UserTable', back_populates='vehicles')
    bookings = relationship('BookingTable', back_populates='vehicle')


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
