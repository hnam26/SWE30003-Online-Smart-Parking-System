from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.parking.parkingLot import ParkingLot
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from DataAccessLayer.models import parkingSlot
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal.invoice import Invoice
from DataAccessLayer.payment.payment import Payment

from typing import List


class Services:
    def __init__(self):
        self.__db = DatabaseAccess()

    def getAllAvailableParkingSlots(self):
        session = self.__db.getSession()
        try:
            available_slots = session.query(parkingSlot.ParkingSlot).filter_by(is_available=True).all()
            return available_slots
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            session.close()

    def viewAvailableParkingSlots(self):
        availableSlots = self.getAllAvailableParkingSlots()

        if availableSlots:
            print("\nAvailable Parking Slots:")
            for slot in availableSlots:
                print(f"Location: {slot.slot_number}")
            else:
                print("\nNo available parking slots.")

    # def getAllAvailableSlots(parkingLot: ParkingLot) -> List[ParkingSlot]:
    #     return [slot for slot in parkingLot.getAllSlots() if slot.getIsAvailable()]

