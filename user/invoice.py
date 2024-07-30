from payment.payment import Payment
from database.databaseAccess import DatabaseAccess
class Invoice:
  def __init__(self, payment: Payment, database: DatabaseAccess):
    self._payment = payment
    self.__database = database

  def generateInvoice(self):
    fee = self._payment.getAmount()
    return fee
  