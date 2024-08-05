from DataAccessLayer.database.databaseAccess import DatabaseAccess
from sqlalchemy import text
from DataAccessLayer.report.report import Report
from tabulate import tabulate

class ManagementReport(Report):
    def __init__(self):
        super().__init__()
        self.__db = DatabaseAccess()

    def generateReport(self, user_id=None):
        session = self.__db.getSession()
        try:
            # Query for total revenue
            revenueQuery = text("SELECT SUM(amount) as total_revenue FROM Payment")
            revenueResult = session.execute(revenueQuery).scalar()

            # Query for slot availability
            occupiedSlotsQuery = text("SELECT COUNT(*) FROM ParkingSlot WHERE is_available = FALSE")
            occupiedSlotsResult = session.execute(occupiedSlotsQuery).scalar()

            availableSlotsQuery = text("SELECT COUNT(*) FROM ParkingSlot WHERE is_available = TRUE")
            availableSlotsResult = session.execute(availableSlotsQuery).scalar()

            # Query for revenue details
            revenueDetailsQuery = text("SELECT payment_date, amount FROM Payment")
            revenueDetailsResult = session.execute(revenueDetailsQuery).mappings().all()
            revenueDetails = [dict(detail) for detail in revenueDetailsResult]

            # Query for booking trends
            bookingTrendsQuery = text("SELECT start_time FROM Booking")
            bookingTrendsResult = session.execute(bookingTrendsQuery).mappings().all()
            bookingTrends = [dict(trend) for trend in bookingTrendsResult]

            revenue_stats = f"Total Revenue: {revenueResult}\n"
            revenue_details = tabulate(
                revenueDetails,
                headers={"payment_date": "Payment Date", "amount": "Amount"},
                tablefmt="grid"
            )
            booking_trends_stats = tabulate(
                bookingTrends,
                headers={"start_time": "Start Time"},
                tablefmt="grid"
            )

            self.content = (
                f"Occupied Slots: {occupiedSlotsResult}\n"
                f"Available Slots: {availableSlotsResult}\n"
                + revenue_stats
                + "\nRevenue Details:\n" + revenue_details
                + "\nBooking Trends:\n" + booking_trends_stats
            )
        except Exception as e:
            self.content = f"An error occurred: {e}"
        finally:
            session.close()

    def printReport(self):
        self.generateReport()
        print(self.content)
