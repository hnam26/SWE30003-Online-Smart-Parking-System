from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.user.invoice import Invoice


class InvoiceServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    @staticmethod
    def generateInvoice(invoice: Invoice):
        return invoice.getAmount()
