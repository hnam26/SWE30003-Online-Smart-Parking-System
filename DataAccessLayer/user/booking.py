from user import User
from parking.parkingSlot import ParkingSlot
from payment.payment import Payment
from invoice import Invoice
class Booking:
    def __init__(self, user: User, duration: int, parkingSlot: ParkingSlot):
        self.__isLateCheckOut = False
        self._user = user
        self._duration = duration
        self._parkingSlot = parkingSlot
        self.__isPaymentSuccessful = False
        self.__isCheckInSuccessful = False

    def getUser(self) -> User:
        return self._user
    
    def getDuration(self) -> int:
        return self._duration
    
    def getParkingSlot(self) -> ParkingSlot:
        return self._parkingSlot
    
    def calculateFee(self) -> int:
        # Calculate the fee based on the duration
        # Fee is $10 per hour
        if self.__isLateCheckOut:
            return self._duration * 10 + 10
        return self._duration * 10

    def makePayment(self, payment: Payment) -> bool:
        # Make payment using the payment method
        # If paymentMethod is Visa, call the Visa class's payment method
        # If paymentMethod is MasterCard, call the MasterCard class's payment method

        payment.process_payment(self)
       
        self.__isPaymentSuccessful = payment.process_payment(self)
    
        if not self.__isPaymentSuccessful:
            return False
        
        invoice = Invoice(payment)

        self._parkingSlot.setIsAvailable(False)

        return self.__isPaymentSuccessful, invoice.generateInvoice()

    def isPaymentSuccessful(self) -> bool:
        return self.__isPaymentSuccessful
    
    def checkIn(self) -> bool:
        # Check-in the user
        # If the payment is successful, check-in the user
        if not self.__isPaymentSuccessful:
            return False
        
        self.__isCheckInSuccessful = True
        return True
    
    def isCheckInSuccessful(self) -> bool:
        return self.__isCheckInSuccessful
    
    def checkLateCheckOut(self) -> bool:
        # query database for start time of booking, compare with current time
        # if current time - start time > duration, return True
        # else call calculateFee() and makePayment() with the additional fee

        pass

    
    def checkOut(self):
        # if self.validateCheckoutConditions():
        #     self._parkingSlot.setIsAvailable(True)
        #     return True
        # return False
        if not self.validateCheckoutConditions():
            return False
        
        self._parkingSlot.setIsAvailable(True)
        return True
        
    def validateCheckoutConditions(self):
        if self.__isCheckInSuccessful and self.__isPaymentSuccessful and not self.__isLateCheckOut:
            return True
        return False