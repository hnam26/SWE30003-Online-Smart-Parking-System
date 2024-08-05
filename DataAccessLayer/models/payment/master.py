from payment import Payment


class Master(Payment):

    def processPayment(self, **kwargs) -> bool:
        # Process the payment using the credit card
        # fee: 2
        return True
