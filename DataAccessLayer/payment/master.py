from payment import Payment


class Master(Payment):
    def __init__(self, amount: int):
        super().__init__(amount)

    def processPayment(self, **kwargs) -> bool:
        # Process the payment using the credit card
        # fee: 2
        return True
