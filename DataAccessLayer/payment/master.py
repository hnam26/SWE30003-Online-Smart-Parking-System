from payment.payment import Payment

class Master(Payment):
    def __init__(self, amount: int):
        super().__init__(amount)

    def processPayment(self) -> bool:
        # Process the payment using the credit card
        # fee: 2
        return True



