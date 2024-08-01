from DataAccessLayer.database import databaseAccess
from DataAccessLayer.database.databaseAccess import Payment
from DataAccessLayer.parking.parkingLot import ParkingLot
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal.invoice import Invoice
from DataAccessLayer.payment.payment import Payment

from typing import List


def getAllAvailableSlots(parkingLot: ParkingLot) -> List[ParkingSlot]:
    return [slot for slot in parkingLot.getAllSlots() if slot.getIsAvailable()]






