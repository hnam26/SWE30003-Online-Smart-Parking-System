from payment import Payment


class Visa(Payment):
    def __init__(self, amount: int):
        super().__init__(amount)

    def processPayment(self, **kwargs) -> bool:
        # Process the payment using the visa card
        # fee: 1
        return True
