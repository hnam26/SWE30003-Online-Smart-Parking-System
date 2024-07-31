from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.user.booking import Booking
from DataAccessLayer.payment.payment import Payment
from DataAccessLayer.user.invoice import Invoice
from invoiceServices import InvoiceServices


class BookingServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    @staticmethod
    def calculateFee(booking: Booking) -> int:
        # Calculate the fee based on the duration
        # Fee is $10 per hour
        if booking.isLateCheckOut():
            return booking.getDuration() * 10 + 10
        return booking.getDuration() * 10

    def makePayment(self, booking: Booking, payment: Payment) -> bool:
        paymentStatus = payment.processPayment(booking, self.calculateFee(booking))
        booking.setPaymentStatus(paymentStatus)

        if not booking.isPaymentSuccessful():
            return False

        booking.getParkingSlot().setIsAvailable(False)
        invoiceServices = InvoiceServices()
        return invoiceServices.generateInvoice(Invoice(payment))

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
