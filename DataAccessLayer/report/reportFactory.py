from DataAccessLayer.report.userReport import UserReport
from DataAccessLayer.report.managementReport import ManagementReport
# from DataAccessLayer.database.databaseAccess import DatabaseAccess
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class ReportTypeTable(Base):
    __tablename__ = 'ReportType'
    report_type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False)
    reports = relationship('ReportTable', back_populates='report_type')


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
        
        if reportType.lower() == "personal":
            return UserReport(ReportFactory._dbInstance)
        elif reportType.lower() == "management":
            return ManagementReport(ReportFactory._dbInstance)
        else:
            raise ValueError(f"Unknown report type: {reportType}")

    @staticmethod
    def generate_and_print_report(reportType, user_id=None):
        """Generate and print the specified report."""
        report = ReportFactory.create_report(reportType)
        if reportType.lower() == "personal" and user_id is not None:
            report.printReport(user_id)
        else:
            report.printReport()

    @staticmethod
    def run_report_generation():
        """Method to handle personal input and generate reports."""
        try:
            # Get the personal ID from the personal input
            user_id = int(input("Enter the personal ID for the personal report: "))

            # Generate and print personal report
            print("\nUser Report:")
            ReportFactory.generate_and_print_report("personal", user_id)
        except ValueError:
            print("Invalid personal ID. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

        # Generate and print management report
        print("\nManagement Report:")
        try:
            ReportFactory.generate_and_print_report("management")
        except Exception as e:
            print(f"An error occurred: {e}")
