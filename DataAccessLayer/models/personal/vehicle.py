from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import relationship
from DataAccessLayer.models.base import Base
from DataAccessLayer.models.utils.typesOfVehicle import TypesOfVehicle


class Vehicle(Base):
    __tablename__ = 'Vehicle'
    __vehicleId = Column("vehicle_id", Integer, primary_key=True, autoincrement=True)
    __userId = Column("user_id", Integer, ForeignKey('User.user_id'), nullable=False)
    __licensePlate = Column("license_plate", String(20), unique=True, nullable=False)
    __vehicleType = Column("vehicle_type", SqlEnum(TypesOfVehicle), nullable=False)

    user = relationship('User', back_populates='vehicles')
    bookings = relationship('Booking', back_populates='vehicle')


    def __init__(self, userId, licensePlate, vehicleType):
        self.__userId = userId
        self.__licensePlate = licensePlate
        self.__vehicleType = vehicleType

        
    @property
    def getLicensePlate(self):
        return self.__licensePlate

    @property
    def getVehicleType(self):
        return self.__vehicleType
    
    @property
    def getUserId(self):
        return self.__userId
