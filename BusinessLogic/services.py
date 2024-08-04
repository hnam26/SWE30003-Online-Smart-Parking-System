from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.personal.invoice import Invoice
from DataAccessLayer.payment.payment import Payment


class Services:
    def __init__(self):
        self.__db = DatabaseAccess()
