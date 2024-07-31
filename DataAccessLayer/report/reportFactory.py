from DataAccessLayer.report.userReport import UserReport
from DataAccessLayer.report.managementReport import ManagementReport
from DataAccessLayer.database.databaseAccess import DatabaseAccess

class ReportFactory:
    _db_instance = None  # Class variable to hold the database instance

    @staticmethod
    def initialize_database(connection_string):
        """Initialize the database instance."""
        if ReportFactory._db_instance is None:
            ReportFactory._db_instance = DatabaseAccess(connection_string)
        else:
            raise ValueError("Database has already been initialized.")

    @staticmethod
    def create_report(report_type):
        """Create a report object based on the report type."""
        if ReportFactory._db_instance is None:
            raise ValueError("Database has not been initialized. Call initialize_database() first.")
        
        if report_type.lower() == "user":
            return UserReport(ReportFactory._db_instance)
        elif report_type.lower() == "management":
            return ManagementReport(ReportFactory._db_instance)
        else:
            raise ValueError(f"Unknown report type: {report_type}")

    @staticmethod
    def generate_and_print_report(report_type, user_id=None):
        """Generate and print the specified report."""
        report = ReportFactory.create_report(report_type)
        if report_type.lower() == "user" and user_id is not None:
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
