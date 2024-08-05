from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.report.report import Report
from DataAccessLayer.models.personal.user import User
from DataAccessLayer.models.personal.booking import Booking
from sqlalchemy import text
from tabulate import tabulate
import sys

class UserReport(Report):
    def __init__(self):
        super().__init__()
        self.__db = DatabaseAccess()

    def generateReport(self, userId: int=None):
        session = self.__db.getSession()
        try:
            for user in session.query(User).all():
                if user.getUserId == userId:
                    break
            # print(user.__dict__)

            if user:
                user_info = f"""
Full Name: {user.getFirstName} {user.getLastName}
Contact:
    - Email: {user.getEmail}
    - Phone Number: {user.getPhone}
"""
                        
                bookings = [{
                    "bookingId": booking.getBookingId,
                    "parkingSlotId": booking.getParkingSlot.getSlotNumber,
                    "vehicle": f"{booking.getVehicle.getLicensePlate} ({booking.getVehicle.getVehicleType.value})",
                    "startTime": booking.getStartTime,
                    "duration": booking.getDuration,
                    "status": booking.getStatus
                    } for booking in user.getBookings]
                # print(bookings)

                booking_history = tabulate(
                    bookings,
                    headers={
                        "bookingId": "Booking ID", 
                        "parkingSlotId": "Slot",
                        "vehicle": "Vehicle",
                        "startTime": "Start Time", 
                        "duration": "Duration",
                        "status": "Status"
                        },
                    tablefmt="grid"
                )
                
                # print(booking_history)

                payments = [{
                    "paymentId": payment.getPaymentId,
                    "bookingId": payment.getBooking.getBookingId,
                    "amount": payment.getAmount,
                    "paymentMethod": payment.getPaymentMethod,
                    "paymentDate": payment.getPaymentDate
                    } for payment in user.getPayment]

                payment_history = tabulate(
                    payments,
                    headers={
                        "paymentId": "Payment ID", 
                        "bookingId": "Booking ID",
                        "amount": "Amount", 
                        "paymentMethod": "Payment Method",
                        "paymentDate": "Date"
                        },
                    tablefmt="grid"
                )

                self.content = user_info + "\n\nBooking History:\n" + booking_history + "\n\nPayments:\n" + payment_history
            else:
                self.content = "User not found."
        except Exception as e:
            raise e
            self.content = f"An error occurred: {e}"
        finally:
            session.close()

    def printReport(self, userId=None):
        self.generateReport(userId)
        sys.stdout.reconfigure(encoding='utf-8')
        print(self.content)
