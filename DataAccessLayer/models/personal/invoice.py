from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass


class Invoice:
    def __init__(self, payment: 'Payment'):
        self.__payment = payment
        self.__amount = payment.getAmount()

    def getAmount(self) -> float:
        return self.__amount

    def getPayment(self) -> 'Payment':
        return self.__payment
