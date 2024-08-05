from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.personal.booking import Booking
from DataAccessLayer.models.payment.payment import Payment
from .invoiceServices import InvoiceServices


class BookingServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.__session = self.__db.getSession()

    @staticmethod
    def calculateFee(booking: Booking) -> int:
        # Calculate the fee based on the duration
        # Fee is $10 per hour
        if booking.isLateCheckOut():
            return booking.getDuration() * 10 + 10
        return booking.getDuration() * 10

    def makePayment(self, booking: Booking, payment: Payment) -> bool:
        try:
            print(booking, payment)
            fee = self.calculateFee(booking)
            paymentStatus = payment.processPayment(booking, fee)
            booking.setPaymentStatus(paymentStatus)

            if not booking.isPaymentSuccessful():
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
            raise e
            print(f"An error occurred: {e}")
            return False
        finally:
            self.__session.close()


    @staticmethod
    def checkIn(booking: Booking) -> bool:
        if not booking.isPaymentSuccessful():
            return False

        booking.setCheckInStatus(True)
        return True

    @staticmethod
    def validateCheckoutConditions(booking: Booking) -> bool:
        if booking.isPaymentSuccessful() and booking.isCheckInSuccessful() and not booking.isLateCheckOut():
            return True

        return False

    def checkOut(self, booking: Booking) -> bool:
        self.checkLateCheckOut()
        if not self.validateCheckoutConditions(booking):
            return False

        booking.getParkingSlot().setIsAvailable(True)
        return True

    def checkLateCheckOut(self) -> bool:
        pass
