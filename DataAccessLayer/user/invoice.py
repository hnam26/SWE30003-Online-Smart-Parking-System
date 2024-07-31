from DataAccessLayer.payment.payment import Payment
class Invoice:
  def __init__(self, payment: Payment):
    self._payment = payment

  def generateInvoice(self):
    fee = self._payment.getAmount()
    return fee
  
