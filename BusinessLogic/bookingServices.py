from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.models.personal.booking import Booking, BookingStatus
from DataAccessLayer.models.payment.payment import Payment
from DataAccessLayer.models.parking.parkingSlot import ParkingSlot
from .invoiceServices import InvoiceServices
from datetime import datetime
from sqlalchemy import update

class BookingServices:
    def __init__(self):
        self.__db = DatabaseAccess()
        self.__session = self.__db.getSession()

    @staticmethod
    def calculateFee(booking: Booking, duration = None, isLateCheckOut: bool = False) -> int:
        # Calculate the fee based on the duration 
        # Fee is $10 per hour

        if isLateCheckOut:
            duration = booking.getDuration

            current_time = datetime.now()
            start_time = booking.getStartTime

            # Assuming start_time and duration are datetime objects or can be converted to datetime
            elapsed_time = (current_time - start_time).total_seconds() / 3600  # Convert to hours
            total_duration = (elapsed_time) + float(duration)

            return int(total_duration * 10 + 10)
        return duration * 10

    def makePayment(self, booking: Booking, duration: int = None, isLateCheckOut: bool = False) -> bool:
        try:
            
            fee = self.calculateFee(booking, duration, isLateCheckOut)
            payment = Payment(input("Please Select your Payment Method: Visa or Master\n"), fee, booking)
            
            if not payment.processPayment(booking, fee):
                return False

            if isLateCheckOut and payment.processPayment(booking, fee):
                return True
            
            booking.setStatus = BookingStatus.PAID.value

            # self.__session.execute(
            # update(Booking).
            # where(Booking.getBookingId == booking.getBookingId).
            # values(status="PAID")
            # )

            if not booking.getStatus == "PAID":
                return False

            parkingSlots = self.__session.query(ParkingSlot).all()
            for parkingSlot in parkingSlots:
                if parkingSlot.getParkingSlotId == booking.getParkingSlotId:
                    break
            parkingSlot.setIsAvailable = False
            # self.__session.execute(
            #     update(ParkingSlot).
            #     where(ParkingSlot.getParkingSlotId == parkingSlot.getParkingSlotId).
            #     values(is_available=False)
            # )

            invoiceServices = InvoiceServices()
            invoiceCreated = invoiceServices.generateInvoice(payment)

            if not invoiceCreated:
                self.__session.rollback()
                return False

            # self.__session.add(payment)            

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

    def checkIn(self, bookingId: Booking) -> bool:
        bookings = self.__session.query(Booking).all()
        
        for booking in bookings:
            if booking.getBookingId == bookingId:
                booking = booking
                break

        if not booking.getStatus == "PAID":
            print("unpaid")
            return False

        # self.__session.execute(
        #     update(Booking).
        #     where(Booking.getBookingId == bookingId).
        #     values(status="IN")
        # )


        booking.setStatus = BookingStatus.IN.value
        return True

    def checkOut(self, bookingId: int) -> bool:

        bookings = self.__session.query(Booking).all()
        for booking in bookings:
            if booking.getBookingId == bookingId:
                break
    
        if self.checkLateCheckOut(booking):
            print("You Check Out Late. Please Pay the Extra Fee")
            if not self.makePayment(booking, isLateCheckOut=True):
                return False
    
        parkingSlots = self.__session.query(ParkingSlot).all()
        for parkingSlot in parkingSlots:
            if parkingSlot.getParkingSlotId == booking.getParkingSlotId:
                break

        parkingSlot.setIsAvailable = True
        # print(parkingSlot.getParkingSlotId)
        
        # self.__session.execute(
        #     update(ParkingSlot).
        #     where(ParkingSlot.getParkingSlotId == parkingSlot.getParkingSlotId).
        #     values(is_available=True)
        # )
        
        self.__session.commit()

        # booking.setStatus = BookingStatus.OUT.value
        # self.__session.execute(
        #     update(Booking).
        #     where(Booking.getBookingId == bookingId).
        #     values(status="OUT")
        # )

        return True


    @staticmethod
    def checkLateCheckOut(booking: Booking) -> bool:
        current_time = datetime.now()
        start_time = booking.getStartTime
        duration = booking.getDuration

        # Assuming start_time and duration are datetime objects or can be converted to datetime
        elapsed_time = (current_time - start_time).total_seconds() / 3600  # Convert to hours

        if elapsed_time > duration:
            return True

        return False
