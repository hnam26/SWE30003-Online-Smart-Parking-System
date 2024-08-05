from DataAccessLayer.models.parking.parkingSlot import ParkingSlot
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass


class Booking:
    def __init__(self, user: 'User', duration: int, parkingSlot: ParkingSlot):
        self.__isLateCheckOut = False
        self.__user = user
        self.__duration = duration
        self.__parkingSlot = parkingSlot
        self.__isPaymentSuccessful = False
        self.__isCheckInSuccessful = False

    def getUser(self) -> 'User':
        return self.__user
    
    def getDuration(self) -> int:
        return self.__duration
    
    def getParkingSlot(self) -> ParkingSlot:
        return self.__parkingSlot

    def isPaymentSuccessful(self) -> bool:
        return self.__isPaymentSuccessful

    def setPaymentStatus(self, status: bool) -> None:
        self.__isPaymentSuccessful = status

    def isCheckInSuccessful(self) -> bool:
        return self.__isCheckInSuccessful

    def setCheckInStatus(self, status: bool) -> None:
        self.__isCheckInSuccessful = status
    
    def isLateCheckOut(self) -> bool:
        return self.__isLateCheckOut

    def setLateCheckOut(self, status: bool) -> None:
        self.__isLateCheckOut = status
