from sqlalchemy.orm import declarative_base

Base = declarative_base()

from DataAccessLayer.models.user import User
from DataAccessLayer.models.vehicle import Vehicle
from DataAccessLayer.models.booking import Booking
from DataAccessLayer.models.invoice import Invoice
from DataAccessLayer.models.payment import Payment
from DataAccessLayer.models.report import Report
from DataAccessLayer.models.reportType import ReportType
from DataAccessLayer.models.parkingLot import ParkingLot
from DataAccessLayer.models.parkingSlot import ParkingSlot