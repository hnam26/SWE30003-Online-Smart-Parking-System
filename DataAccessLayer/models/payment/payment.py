from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from DataAccessLayer.models.personal.invoice import Invoice


class Payment(ABC):
    def __init__(self, amount: int):
        self.__amount = amount
        self.__invoice = Invoice(self)

    @abstractmethod
    def processPayment(self, booking, amount) -> bool:
        """
    This method is intended to be implemented by subclasses to handle specific payment processing logic.
    It should attempt to process the payment for the provided Booking object and amount,
    returning True on success and False on failure.
    """
        pass

    def getAmount(self) -> float:
        return self.__amount

    def getInvoice(self) -> 'Invoice':
        return self.__invoice
