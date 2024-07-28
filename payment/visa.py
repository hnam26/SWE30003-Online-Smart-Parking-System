from payment.payment import Payment

class Visa(Payment):
    def __init__(self, amount: int):
        super().__init__(amount)

    def process_payment(self) -> bool:
        # Process the payment using the visa card
        # fee: 1
        return True