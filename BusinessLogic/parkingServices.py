from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.parkingSlot import ParkingSlot as modelSlot
from DataAccessLayer.models.parkingLot import ParkingLot as modelLot
from DataAccessLayer.models.parking import ParkingSlot
from DataAccessLayer.models.parking import ParkingLot
from tabulate import tabulate
from typing import Union


class ParkingServices:
    def __init__(self):
        # print("Initializing Parking Services...")
        self.__db = DatabaseAccess()
        self.session = self.__db.getSession()
        self.repo: list[ParkingLot] = []
        self.initialize()

    def getSession(self):
        return self.__db.getSession()

    def initialize(self):
        parking_lots = self.session.query(modelLot).all()
        for lot in parking_lots:
            slots = self.session.query(modelSlot).filter_by(parking_lot_id=lot.parking_lot_id).all()
            # print(type(slots[0]))
            parking_lot = ParkingLot(
                name=lot.name,
                slots=[self.responseParkingSlot(slot) for slot in slots],
                location=lot.location
            )
            # print(type(parking_lot.getAllSlots()[0]))
            self.repo.append(parking_lot)
        # print("Parking Lots initialized successfully. Length: ", len(self.repo), type(self.repo[0]), type(self.repo[0].getAllSlots()[0]))

    def responseParkingLot(self, parkingLot: modelLot) -> ParkingLot:
        return ParkingLot(
            name=parkingLot.name,
            slots=next(lot for lot in self.repo if lot.name == parkingLot.name).slots,
            location=parkingLot.location
        )
        
    def responseParkingSlot(self, parkingSlot: modelSlot) -> ParkingSlot:
        return ParkingSlot(
            slotNumber=parkingSlot.slot_number,
            isAvailable=parkingSlot.is_available,
            parkingLotId=parkingSlot.parking_lot_id
        )

    def getParkingSlotByNumber(self, slotNumber: str) -> Union[modelSlot, None]:
        try:
            for lot in self.repo:
                for slot in lot.getAllSlots():
                    if slot.getSlotNumber() == slotNumber:
                        return slot
            return None
        except Exception as e:
            raise e
            print(f"An error occurred while fetching the parking slot: {e}")
            return None
        finally:
            self.session.close()

    def getAllAvailableParkingSlots(self) -> Union[dict[ParkingLot, list[ParkingSlot]], None]:
        try:
            parkingLotDict = {}
            for lot in self.repo:
                parkingLotDict[lot] = [slot for slot in lot.getAllSlots()]
            return parkingLotDict
        except Exception as e:
            raise e
            print(f"An error occurred: {e}")
            return None
        finally:
            self.session.close()

    def viewAvailableParkingSlots(self):
        parkingLotDict = self.getAllAvailableParkingSlots()

        if not parkingLotDict:
            print("\nNo available parking slots.")
        else:
            for lot, slots in parkingLotDict.items():
                print(f"\nParking Lot: {lot.getLocation()}")
                table = [[slot.getSlotNumber()] for slot in slots]
                print(tabulate(table, headers=["Slot Number", "Location"], tablefmt="grid"))
