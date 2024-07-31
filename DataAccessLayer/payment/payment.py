from abc import ABC, abstractmethod


class Payment(ABC):
    def __init__(self, amount: int):
        self.__amount = amount

    @abstractmethod
    def processPayment(self, booking, amount) -> bool:
        """
    This method is intended to be implemented by subclasses to handle specific payment processing logic.
    It should attempt to process the payment for the provided Booking object and amount,
    returning True on success and False on failure.
    """
        pass

    def getAmount(self):
        return self.__amount
