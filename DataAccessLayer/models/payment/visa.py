from payment import Payment


class Visa(Payment):
    def processPayment(self, **kwargs) -> bool:
        # Process the payment using the visa card
        # fee: 1
        return True
