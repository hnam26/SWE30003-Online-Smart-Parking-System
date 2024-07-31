from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.user.booking import Booking
from DataAccessLayer.payment.payment import Payment
from DataAccessLayer.user.invoice import Invoice

class BookingServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    
    def calculateFee(self, booking: Booking) -> int:
        # Calculate the fee based on the duration
        # Fee is $10 per hour
        if booking.isLateCheckOut():
            return booking.getDuration() * 10 + 10
        return booking.getDuration() * 10

    def makePayment(self, booking: Booking, payment: Payment) -> bool:
        payment = payment.processPayment(booking, self.calculateFee(booking))
        booking.setPaymentStatus(payment)

        if not booking.isPaymentSuccessful():
            return False

        invoice = Invoice(payment)
        booking.getParkingSlot().setIsAvailable(False)

        return invoice.generateInvoice()


    def checkIn(self, booking: Booking) -> bool:
        if not booking.isPaymentSuccessful():
            return False

        booking.setCheckInStatus(True)
        return True


    def validateCheckoutConditions(self, booking: Booking) -> bool:
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
