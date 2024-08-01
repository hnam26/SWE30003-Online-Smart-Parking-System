from DataAccessLayer.report.userReport import UserReport
from DataAccessLayer.report.managementReport import ManagementReport
from DataAccessLayer.database.databaseAccess import DatabaseAccess

class ReportFactory:
    _dbInstance = None  # Class variable to hold the database instance

    @staticmethod
    def initialize_database(connectionString):
        """Initialize the database instance."""
        if ReportFactory._dbInstance is None:
            ReportFactory._dbInstance = DatabaseAccess(connectionString)
        else:
            raise ValueError("Database has already been initialized.")

    @staticmethod
    def create_report(reportType):
        """Create a report object based on the report type."""
        if ReportFactory._dbInstance is None:
            raise ValueError("Database has not been initialized. Call initialize_database() first.")
        
        if reportType.lower() == "user":
            return UserReport(ReportFactory._dbInstance)
        elif reportType.lower() == "management":
            return ManagementReport(ReportFactory._dbInstance)
        else:
            raise ValueError(f"Unknown report type: {reportType}")

    @staticmethod
    def generate_and_print_report(reportType, user_id=None):
        """Generate and print the specified report."""
        report = ReportFactory.create_report(reportType)
        if reportType.lower() == "user" and user_id is not None:
            report.printReport(user_id)
        else:
            report.printReport()

    @staticmethod
    def run_report_generation():
        """Method to handle user input and generate reports."""
        try:
            # Get the user ID from the user input
            user_id = int(input("Enter the user ID for the user report: "))

            # Generate and print user report
            print("\nUser Report:")
            ReportFactory.generate_and_print_report("user", user_id)
        except ValueError:
            print("Invalid user ID. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Generate and print management report
        print("\nManagement Report:")
        try:
            ReportFactory.generate_and_print_report("management")
        except Exception as e:
            print(f"An error occurred: {e}")
