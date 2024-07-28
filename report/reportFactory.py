
from userReport import UserReport
from managementReport import ManagementReport

class ReportFactory:
    @staticmethod
    def create_report(report_type, title, data):
        if report_type.lower() == "user":
            return UserReport(title, data)
        elif report_type.lower() == "management":
            return ManagementReport(title, data)
        else:
            raise ValueError(f"Unknown report type: {report_type}")

    @staticmethod
    def generate_and_print_report(report_type, title, data):
        report = ReportFactory.create_report(report_type, title, data)
        report.generate_report()
        print(report.format_report())

# Example usage
if __name__ == "__main__":
    user_data = {
        "name": "John Doe",
        "contact": "john.doe@example.com",
        "bookings": ["Booking1: 01-01-2024, Slot A1", "Booking2: 05-01-2024, Slot B2"],
        "total_paid": "$100",
        "payments": ["Payment1: $50", "Payment2: $50"]
    }
    
    management_data = {
        "occupied_slots": 120,
        "available_slots": 30,
        "total_revenue": "$3000",
        "revenue_details": ["Jan: $1000", "Feb: $2000"],
        "booking_trends": ["Morning Peak: 8-10 AM", "Evening Peak: 6-8 PM"]
    }
    
    # Generate and print user report
    ReportFactory.generate_and_print_report("user", "User Report", user_data)
    
    # Generate and print management report
    ReportFactory.generate_and_print_report("management", "Monthly Management Report", management_data)
