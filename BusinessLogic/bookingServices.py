from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.personal.booking import Booking
from DataAccessLayer.payment.payment import Payment
from .invoiceServices import InvoiceServices


class BookingServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.session = self.__db.getSession()

    @staticmethod
    def calculateFee(booking: Booking) -> int:
        # Calculate the fee based on the duration
        # Fee is $10 per hour
        if booking.isLateCheckOut():
            return booking.getDuration() * 10 + 10
        return booking.getDuration() * 10

    def makePayment(self, booking: Booking, payment: Payment) -> bool:
        try:
            fee = self.calculateFee(booking)
            # payment = Payment(booking=booking, payment_method=paymentMethod, amount=fee, payment_date=datetime.now())
            paymentStatus = payment.processPayment(booking, fee)
            booking.setPaymentStatus(paymentStatus)

            if not booking.isPaymentSuccessful():
                return False

            booking.getParkingSlot().setIsAvailable(False)
            invoiceServices = InvoiceServices()
            invoiceCreated = invoiceServices.generateInvoice(payment.getInvoice())

            if not invoiceCreated:
                self.session.rollback()
                return False

            self.session.add(payment)
            self.session.commit()
            print("Payment record saved to the database.")
            return True
        except Exception as e:
            self.session.rollback()
            print(f"An error occurred: {e}")
            return False
        finally:
            self.session.close()
        # paymentStatus = payment.processPayment(booking, self.calculateFee(booking))
        # booking.setPaymentStatus(paymentStatus)
        #
        # if not booking.isPaymentSuccessful():
        #     return False
        #
        # booking.getParkingSlot().setIsAvailable(False)
        # invoiceServices = InvoiceServices()
        # return invoiceServices.generateInvoice(Invoice(payment))

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
