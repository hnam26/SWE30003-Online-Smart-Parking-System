from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import threading
from DataAccessLayer.personal.user import UserTable
from DataAccessLayer.personal.vehicle import VehicleTable
from DataAccessLayer.personal.booking import BookingTable
from DataAccessLayer.personal.invoice import InvoiceTable
from DataAccessLayer.payment.payment import PaymentTable
from DataAccessLayer.report.report import ReportTable
from DataAccessLayer.report.reportFactory import ReportTypeTable
from DataAccessLayer.parking.parkingLot import ParkingLotTable
from DataAccessLayer.parking.parkingSlot import ParkingSlotTable

# Collect all Base classes
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# List all the table classes
table_classes = [
    UserTable,
    VehicleTable,
    BookingTable,
    PaymentTable,
    InvoiceTable,
    ReportTable,
    ReportTypeTable,
    ParkingLotTable,
    ParkingSlotTable
]

# Dynamically add the tables to the Base metadata
for table_class in table_classes:
    table_class.__table__.metadata = Base.metadata


class DatabaseAccess:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, connection_string='mysql+mysqlconnector://root:*Sinh08062004*@localhost/OSPS'):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(DatabaseAccess, cls).__new__(cls)
                cls.__instance.engine = create_engine(connection_string)
                cls.__instance.Session = sessionmaker(bind=cls.__instance.engine)
                # Ensure the metadata is created using the imported Base
                Base.metadata.create_all(cls.__instance.engine)
                print("Database connection established")
            return cls.__instance

    def getSession(self):
        return self.Session()

    def close(self):
        if self.__instance and self.__instance.engine:
            self.__instance.engine.dispose()
            print("Database connection closed")

