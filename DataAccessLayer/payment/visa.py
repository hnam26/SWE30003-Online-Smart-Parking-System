from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.payment.payment import Payment

class Visa(Payment):
    def __init__(self, amount: int, database: DatabaseAccess):
        super().__init__(amount, database)

    def process_payment(self) -> bool:
        # Process the payment using the visa card
        # fee: 1
        return True