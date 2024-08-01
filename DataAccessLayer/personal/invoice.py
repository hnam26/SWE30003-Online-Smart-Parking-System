from DataAccessLayer.payment.payment import Payment


class Invoice:
    def __init__(self, payment: Payment):
        self._payment = payment
        self._amount = payment.getAmount()

    def getAmount(self) -> float:
        return self._amount
