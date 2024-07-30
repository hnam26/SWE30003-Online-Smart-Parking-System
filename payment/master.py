from database.databaseAccess import DatabaseAccess
from payment.payment import Payment

class Master(Payment):
    def __init__(self, amount: int, database: DatabaseAccess):
        super().__init__(amount, database)


    def processPayment(self) -> bool:
        # Process the payment using the credit card
        # fee: 2
        return True



