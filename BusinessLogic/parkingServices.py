from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models import parkingSlot
from DataAccessLayer.models import parkingLot
from tabulate import tabulate
from typing import List


class ParkingServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    def getAllAvailableParkingSlots(self) -> List[parkingSlot.ParkingSlot]:
        session = self.__db.getSession()
        try:
            availableSlots = session.query(parkingSlot.ParkingSlot).filter_by(is_available=True).all()
            return availableSlots
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
        finally:
            session.close()

    def mapSlotsToParkingLots(self, availableSlots: List[parkingSlot.ParkingSlot]) -> dict:
        session = self.__db.getSession()
        try:
            parkingLotDict = {}
            for slot in availableSlots:
                lot = session.query(parkingLot.ParkingLot).filter_by(parking_lot_id=slot.parking_lot_id).first()
                if lot:
                    if lot not in parkingLotDict:
                        parkingLotDict[lot] = []
                    parkingLotDict[lot].append(slot)
            return parkingLotDict
        except Exception as e:
            print(f"An error occurred: {e}")
            return {}
        finally:
            session.close()

    def viewAvailableParkingSlots(self):
        availableSlots = self.getAllAvailableParkingSlots()
        parkingLotDict = self.mapSlotsToParkingLots(availableSlots)

        if not parkingLotDict:
            print("\nNo available parking slots.")
        else:
            for lot, slots in parkingLotDict.items():
                print(f"\nParking Lot: {lot.location}")
                table = [[slot.slot_number] for slot in slots]
                print(tabulate(table, headers=["Slot Number", "Location"], tablefmt="grid"))



