from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.invoice import Invoice


class InvoiceServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    @staticmethod
    def generateInvoice(invoice: Invoice):
        print(f"The Invoice for Payment{1}", invoice.getPayment())
        print(f"The total amount you need to pay is {1}", invoice.getAmount())
