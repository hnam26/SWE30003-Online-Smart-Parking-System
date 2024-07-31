from user import User
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from DataAccessLayer.payment.payment import Payment
from invoice import Invoice
from DataAccessLayer.database.databaseAccess import DatabaseAccess
class Booking:
    def __init__(self, user: User, duration: int, parkingSlot: ParkingSlot, database: DatabaseAccess):
        self.__isLateCheckOut = False
        self._user = user
        self._duration = duration
        self._parkingSlot = parkingSlot
        self.__database = database
        self.__isPaymentSuccessful = False
        self.__isCheckInSuccessful = False

    def getUser(self) -> User:
        return self._user
    
    def getDuration(self) -> int:
        return self._duration
    
    def getParkingSlot(self) -> ParkingSlot:
        return self._parkingSlot


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
    
    def isLateCheckOut(self) -> bool:
        # query database for start time of booking, compare with current time
        # if current time - start time > duration, return True
        # else call calculateFee() and makePayment() with the additional fee
        return self.__isLateCheckOut
    
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