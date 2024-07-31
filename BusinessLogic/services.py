from DataAccessLayer.database import databaseAccess
from DataAccessLayer.parking.parkingLot import ParkingLot
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from DataAccessLayer.user.booking import Booking

from typing import List


def getAllAvailableSlots(parkingLot: ParkingLot) -> List[ParkingSlot]:
    return [slot for slot in parkingLot.getAllSlots() if slot.getIsAvailable()]

def calculateFee() -> int:
    # Calculate the fee based on the duration
    # Fee is $10 per hour
    if Booking.isLateCheckOut():
        return Booking.getDuration() * 10 + 10
    return Booking.getDuration() * 10