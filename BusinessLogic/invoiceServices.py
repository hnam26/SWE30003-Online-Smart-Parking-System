from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.personal.invoice import Invoice


class InvoiceServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    @staticmethod
    def generateInvoice(payment):
        return "Invoice: Paid", payment

