# from DataAccessLayer.report.userReport import UserReport
# from DataAccessLayer.report.managementReport import ManagementReport
# from DataAccessLayer.database.databaseAccess import DatabaseAccess
#
#
# class ReportFactory:
#     _dbInstance = None  # Class variable to hold the database instance
#
#     @staticmethod
#     def initialize_database(connectionString):
#         """Initialize the database instance."""
#         if ReportFactory._dbInstance is None:
#             ReportFactory._dbInstance = DatabaseAccess(connectionString)
#         else:
#             raise ValueError("Database has already been initialized.")
#
#     @staticmethod
#     def create_report(reportType):
#         """Create a report object based on the report type."""
#         if ReportFactory._dbInstance is None:
#             raise ValueError("Database has not been initialized. Call initialize_database() first.")
#
#         if reportType.lower() == "user":
#             return UserReport()
#         elif reportType.lower() == "management":
#             return ManagementReport()
#         else:
#             raise ValueError(f"Unknown report type: {reportType}")
#
#     @staticmethod
#     def generate_and_print_report(reportType, user_id=None):
#         """Generate and print the specified report."""
#         report = ReportFactory.create_report(reportType)
#         if reportType.lower() == "user" and user_id is not None:
#             report.printReport()
#         else:
#             report.printReport()
#
#     @staticmethod
#     def run_report_generation():
#         """Method to handle personal input and generate reports."""
#         try:
#             # Get the personal ID from the personal input
#             user_id = int(input("Enter the personal ID for the personal report: "))
#
#             # Generate and print personal report
#             print("\nUser Report:")
#             ReportFactory.generate_and_print_report("personal", user_id)
#         except ValueError:
#             print("Invalid personal ID. Please enter a valid number.")
#         except Exception as e:
#             print(f"An error occurred: {e}")
#
#         # Generate and print management report
#         print("\nManagement Report:")
#         try:
#             ReportFactory.generate_and_print_report("management")
#         except Exception as e:
#             print(f"An error occurred: {e}")


# reportFactory.py

from DataAccessLayer.report.userReport import UserReport
from DataAccessLayer.report.managementReport import ManagementReport

class ReportFactory:
    @staticmethod
    def getReport(reportType: str):
        if reportType == 'user':
            return UserReport()
        elif reportType == 'management':
            return ManagementReport()
        else:
            raise ValueError(f"Unknown report type: {reportType}")

    def reportMenu(self):
        while True:
            print("Select Report Type:")
            print("1. User Report")
            print("2. Management Report")
            print("3. Exit")
            choice = input("Enter your choice: ").strip()

            try:
                match choice:

                    case '1':
                        reportType = 'user'
                        try:
                            userId = int(input("Enter the user ID: ").strip())
                        except ValueError:
                            print("Invalid user ID. Please enter a numeric value.")
                            return
                    case '2':
                        reportType = 'management'
                        userId = None  # Management report does not need a user ID
                    case '3':
                        break
                    case default:
                        print("Invalid choice. Please try again.")
                        break

                report = ReportFactory.getReport(reportType)
                if reportType == 'user':
                    report.printReport(userId)
                else:
                    report.printReport()
            except ValueError as e:
                print(e)
