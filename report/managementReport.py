from report import Report

class ManagementReport(Report):
    def __init__(self, title, managementData):
        super().__init__(title)
        self.managementData = managementData

    def generate_report(self):
        usageStats = f"Occupied Slots: {self.managementData['occupied_slots']}\nAvailable Slots: {self.managementData['available_slots']}\n"
        revenueStats = f"Total Revenue: {self.managementData['total_revenue']}\nRevenue Details:\n" + "\n".join(self.managementData['revenue_details']) + "\n"
        bookingTrends = "Booking Trends:\n" + "\n".join(self.managementData['bookingTrends']) + "\n"
        
        self.content = usageStats + revenueStats + bookingTrends
