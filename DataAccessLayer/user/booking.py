from user import User
from DataAccessLayer.parking.parkingSlot import ParkingSlot

class Booking:
    def __init__(self, user: User, duration: int, parkingSlot: ParkingSlot):
        self.__isLateCheckOut = False
        self._user = user
        self._duration = duration
        self._parkingSlot = parkingSlot
        self.__isPaymentSuccessful = False
        self.__isCheckInSuccessful = False

    def getUser(self) -> User:
        return self._user
    
    def getDuration(self) -> int:
        return self._duration
    
    def getParkingSlot(self) -> ParkingSlot:
        return self._parkingSlot


    def isPaymentSuccessful(self) -> bool:
        return self.__isPaymentSuccessful

    def setPaymentStatus(self, status: bool) -> None:
        __isPaymentSuccessful = status

    
    def isCheckInSuccessful(self) -> bool:
        return self.__isCheckInSuccessful

    def setCheckInStatus(self, status: bool) -> None:
        self.__isCheckInSuccessful = status
    
    def isLateCheckOut(self) -> bool:
        return self.__isLateCheckOut

    def setLateCheckOut(self, status: bool) -> None:
        self.__isLateCheckOut = status
