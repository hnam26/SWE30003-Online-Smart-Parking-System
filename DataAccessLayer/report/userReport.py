from DataAccessLayer.report.report import Report
from sqlalchemy import text

class UserReport(Report):
    def __init__(self, db_instance):
        super().__init__()
        self.db = db_instance

    def generateReport(self, user_id):
        session = self.db.getSession()
        try:
            # Query for user data
            user_query = text("SELECT * FROM User WHERE user_id = :user_id")
            user_result = session.execute(user_query, {'user_id': user_id}).mappings().first()

            if user_result:
                user_data = dict(user_result)
                user_info = f"User: {user_data['first_name']} {user_data['last_name']}\nContact: {user_data['email']}, {user_data['phone']}\n"

                # Query for bookings
                bookings_query = text("SELECT * FROM Booking WHERE user_id = :user_id")
                bookings_result = session.execute(bookings_query, {'user_id': user_id}).mappings().all()
                bookings = [dict(booking) for booking in bookings_result]

                booking_history = "Booking History:\n" + "\n".join(
                    [f"Booking ID: {booking['booking_id']}, Slot: {booking['parking_slot_id']}, Start: {booking['start_time']}, Duration: {booking['duration']}" for booking in bookings]) + "\n"

                # Query for payments
                payments_query = text("SELECT * FROM Payment WHERE booking_id IN (SELECT booking_id FROM Booking WHERE user_id = :user_id)")
                payments_result = session.execute(payments_query, {'user_id': user_id}).mappings().all()
                payments = [dict(payment) for payment in payments_result]

                payment_history = "Payments:\n" + "\n".join(
                    [f"Payment ID: {payment['payment_id']}, Amount: {payment['amount']}, Date: {payment['payment_date']}" for payment in payments]) + "\n"

                self.content = user_info + booking_history + payment_history
            else:
                self.content = "User not found."
        except Exception as e:
            self.content = f"An error occurred: {e}"
        finally:
            session.close()

    def printReport(self, user_id):
        self.generateReport(user_id)
        print(self.content)
