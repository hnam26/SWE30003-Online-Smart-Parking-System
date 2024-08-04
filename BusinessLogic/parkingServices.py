from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.parkingSlot import ParkingSlot as modelSlot
from DataAccessLayer.models.parkingLot import ParkingLot as modelLot
from DataAccessLayer.models.parkingSlot import ParkingSlot
from DataAccessLayer.parking.parkingLot import ParkingLot
from tabulate import tabulate
from typing import List, Union


class ParkingServices:
    def __init__(self):
        # print("Initializing Parking Services...")
        self.__db = DatabaseAccess()
        self.session = self.__db.getSession()
        self.repo: list[ParkingLot] = []
        self.initialize()

    def initialize(self):
        parking_lots = self.session.query(modelLot).all()
        for lot in parking_lots:
            slots = self.session.query(modelSlot).filter_by(parking_lot_id=lot.parking_lot_id).all()
            self.repo.append(ParkingLot(
                name=lot.name,
                slots=[self.response_parking_slot(slot) for slot in slots],
                location=lot.location
            ))
        print("Parking Lots initialized successfully. Length: ", len(self.repo), type(self.repo[0]), type(self.repo[0].getAllSlots()[0]))

    def response_parking_lot(self, parking_lot: modelLot) -> ParkingLot:
        return ParkingLot(
            name=parking_lot.name,
            slots=next(lot for lot in self.repo if lot.name == parking_lot.name).slots,
            location=parking_lot.location
        )
        
    def response_parking_slot(self, parking_slot: modelSlot) -> ParkingSlot:
        return ParkingSlot(
            slot_number=parking_slot.slot_number,
            is_available=parking_slot.is_available,
            parking_lot_id=parking_slot.parking_lot_id
        )

    def getParkingSlotByNumber(self, slot_number: str) -> Union[ParkingSlot, None]:
        try:
            parking_slot = self.session.query(ParkingSlot).filter_by(slot_number=slot_number).first()
            return parking_slot
        except Exception as e:
            print(f"An error occurred while fetching the parking slot: {e}")
            return None
        finally:
            self.session.close()

    def getAllAvailableParkingSlots(self) -> Union[dict[ParkingLot, list[ParkingSlot]], None]:
        try:
            # availableSlots = self.session.query(parkingSlot.ParkingSlot).filter_by(is_available=True).all()
            parkingLotDict = {}
            for lot in self.repo:
                parkingLotDict[lot] = [slot for slot in lot.getAllAvailableSlots()]
            return parkingLotDict
        except Exception as e:
            raise e
            print(f"An error occurred: {e}")
            return None
        finally:
            self.session.close()

    # def mapSlotsToParkingLots(self, availableSlots: List[ParkingSlot]) -> dict:
    #     try:
    #         parkingLotDict = {}
    #         for slot in availableSlots:
    #             lot = self.session.query(ParkingLot).filter_by(parking_lot_id=slot.parking_lot_id).first()
    #             if lot:
    #                 if lot not in parkingLotDict:
    #                     parkingLotDict[lot] = []
    #                 parkingLotDict[lot].append(slot)
    #         return parkingLotDict
    #     except Exception as e:
    #         print(f"An error occurred: {e}")
    #         return {}
    #     finally:
    #         self.session.close()

    def viewAvailableParkingSlots(self):
        # availableSlots = self.getAllAvailableParkingSlots()
        # parkingLotDict = self.mapSlotsToParkingLots(availableSlots)
        parkingLotDict = self.getAllAvailableParkingSlots()

        if not parkingLotDict:
            print("\nNo available parking slots.")
        else:
            for lot, slots in parkingLotDict.items():
                print(f"\nParking Lot: {lot.getLocation()}")
                table = [[slot.getSlotNumber()] for slot in slots]
                print(tabulate(table, headers=["Slot Number", "Location"], tablefmt="grid"))
