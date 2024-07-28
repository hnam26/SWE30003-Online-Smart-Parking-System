from Report import Report

class UserReport(Report):
    def __init__(self, title, user_data):
        super().__init__(title)
        self.user_data = user_data

    def generateReport(self):
        userInfo = f"User: {self.user_data['name']}\nContact: {self.user_data['contact']}\n"
        bookingHistory = "Booking History:\n" + "\n".join(self.user_data['bookings']) + "\n"
        paymentHistory = f"Total Paid: {self.user_data['total_paid']}\n" + "Payments:\n" + "\n".join(self.user_data['payments']) + "\n"
        
        self.content = userInfo + bookingHistory + paymentHistory
