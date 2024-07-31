from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.user.booking import Booking
from DataAccessLayer.user.user import User
from DataAccessLayer.parking.parkingSlot import ParkingSlot
from BusinessLogic.bookingServices import BookingServices


class UserServices:
    def __init__(self):
        self.__db = DatabaseAccess()

    def login(self, username, password):
        return self.__db.login(username, password)

    def logout(self):
        return self.__db.logout()

    def makeBooking(self, user: User, parkingSlot: ParkingSlot, duration: int) -> [Booking, bool]:
        if not parkingSlot.getIsAvailable():
            return False

        booking = Booking(user, duration, parkingSlot)
        bookingServices = BookingServices()
        bookingServices.makePayment(booking, user.getPaymentMethod())
        if booking.isPaymentSuccessful():
            user.addBooking(booking)
            # add Booking record to db
            return booking
        return False
