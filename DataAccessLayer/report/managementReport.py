from DataAccessLayer.report.report import Report
from sqlalchemy import text

class ManagementReport(Report):
    def __init__(self, db_instance):
        super().__init__()
        self.db = db_instance

    def generateReport(self):
        session = self.db.getSession()
        try:
            # Query for total revenue
            revenue_query = text("SELECT SUM(amount) as total_revenue FROM Payment")
            revenue_result = session.execute(revenue_query).scalar()

            # Query for slot availability
            occupied_slots_query = text("SELECT COUNT(*) FROM ParkingSlot WHERE is_available = FALSE")
            occupied_slots_result = session.execute(occupied_slots_query).scalar()

            available_slots_query = text("SELECT COUNT(*) FROM ParkingSlot WHERE is_available = TRUE")
            available_slots_result = session.execute(available_slots_query).scalar()

            # Query for revenue details
            revenue_details_query = text("SELECT payment_date, amount FROM Payment")
            revenue_details_result = session.execute(revenue_details_query).mappings().all()
            revenue_details = [dict(detail) for detail in revenue_details_result]

            # Query for booking trends
            booking_trends_query = text("SELECT start_time FROM Booking")
            booking_trends_result = session.execute(booking_trends_query).mappings().all()
            booking_trends = [dict(trend) for trend in booking_trends_result]

            revenue_stats = f"Total Revenue: {revenue_result}\nRevenue Details:\n" + "\n".join(
                [f"{detail['payment_date']}: {detail['amount']}" for detail in revenue_details]) + "\n"
            booking_trends_stats = "Booking Trends:\n" + "\n".join(
                [f"{trend['start_time']}" for trend in booking_trends]) + "\n"

            self.content = f"Occupied Slots: {occupied_slots_result}\nAvailable Slots: {available_slots_result}\n" + revenue_stats + booking_trends_stats
        except Exception as e:
            self.content = f"An error occurred: {e}"
        finally:
            session.close()

    def printReport(self):
        self.generateReport()
        print(self.content)
