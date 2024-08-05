from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.personal.booking import Booking
from DataAccessLayer.models.payment.payment import Payment
from .invoiceServices import InvoiceServices
from datetime import datetime


class BookingServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.__session = self.__db.getSession()

    @staticmethod
    def calculateFee(booking: Booking, isLateCheckOut: bool = False) -> int:
        # Calculate the fee based on the duration
        # Fee is $10 per hour
        if isLateCheckOut:
            current_time = datetime.now()
            start_time = booking.getStartTime()
            duration = booking.getDuration()

            # Assuming start_time and duration are datetime objects or can be converted to datetime
            elapsed_time = (current_time - start_time).total_seconds() / 3600  # Convert to hours
            total_duration = elapsed_time + duration

            return int(total_duration * 10 + 10)
        return booking.getDuration() * 10

    def makePayment(self, booking: Booking, payment: Payment, isLateCheckOut: bool = False) -> bool:
        try:
            print(booking, payment)
            fee = self.calculateFee(booking, isLateCheckOut)
            if not payment.processPayment(booking, fee):
                return False

            booking.setStatus("PAID")

            # update and commit to db

            if not booking.getStatus() == "PAID":
                return False

            booking.getParkingSlot().setIsAvailable(False)
            invoiceServices = InvoiceServices()
            invoiceCreated = invoiceServices.generateInvoice(payment.getInvoice())

            if not invoiceCreated:
                self.__session.rollback()
                return False

            self.__session.add(payment)
            self.__session.commit()
            print("Payment record saved to the database.")
            return True
        except Exception as e:
            self.__session.rollback()
            print(f"An error occurred: {e}")
            raise e
            # return False
        finally:
            self.__session.close()

    @staticmethod
    def checkIn(booking: Booking) -> bool:
        if not booking.getStatus() == "PAID":
            return False

        booking.setStatus("IN")
        return True

    def checkOut(self, booking: Booking, payment: Payment) -> bool:
        if self.checkLateCheckOut(booking):
            print("You Check Out Late. Please Pay the Extra Fee")
            if not self.makePayment(booking, payment, isLateCheckOut=True):
                return False

        booking.getParkingSlot().setIsAvailable(True)
        booking.setStatus("OUT")
        return True


    @staticmethod
    def checkLateCheckOut(booking: Booking) -> bool:
        current_time = datetime.now()
        start_time = booking.getStartTime()
        duration = booking.getDuration()

        # Assuming start_time and duration are datetime objects or can be converted to datetime
        elapsed_time = (current_time - start_time).total_seconds() / 3600  # Convert to hours

        if elapsed_time > duration:
            return True

        return False
