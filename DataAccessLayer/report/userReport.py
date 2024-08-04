from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.report.report import Report
from sqlalchemy import text
from tabulate import tabulate

class UserReport(Report):
    def __init__(self):
        super().__init__()
        self.__db = DatabaseAccess()

    def generateReport(self, user_id=None):
        session = self.__db.getSession()
        try:
            # Query for personal data
            user_query = text("SELECT * FROM User WHERE user_id = :user_id")
            user_result = session.execute(user_query, {'user_id': user_id}).mappings().first()

            if user_result:
                user_data = dict(user_result)
                user_info = f"User: {user_data['first_name']} {user_data['last_name']}\nContact: {user_data['email']}, {user_data['phone']}\n"

                # Query for bookings
                bookings_query = text("SELECT * FROM Booking WHERE user_id = :user_id")
                bookings_result = session.execute(bookings_query, {'user_id': user_id}).mappings().all()
                bookings = [dict(booking) for booking in bookings_result]

                booking_history = tabulate(
                    bookings,
                    headers={"booking_id": "Booking ID", "parking_slot_id": "Slot", "start_time": "Start Time", "duration": "Duration"},
                    tablefmt="grid"
                )

                # Query for payments
                payments_query = text("SELECT * FROM Payment WHERE booking_id IN (SELECT booking_id FROM Booking WHERE user_id = :user_id)")
                payments_result = session.execute(payments_query, {'user_id': user_id}).mappings().all()
                payments = [dict(payment) for payment in payments_result]

                payment_history = tabulate(
                    payments,
                    headers={"payment_id": "Payment ID", "amount": "Amount", "payment_date": "Date"},
                    tablefmt="grid"
                )

                self.content = user_info + "\nBooking History:\n" + booking_history + "\n\nPayments:\n" + payment_history
            else:
                self.content = "User not found."
        except Exception as e:
            self.content = f"An error occurred: {e}"
        finally:
            session.close()

    def printReport(self, user_id=None):
        self.generateReport(user_id)
        print(self.content)
