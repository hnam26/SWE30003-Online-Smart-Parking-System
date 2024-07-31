from DataAccessLayer.report.userReport import UserReport
from DataAccessLayer.report.managementReport import ManagementReport

class ReportFactory:
    connection_string = 'mysql+mysqlconnector://root:12345@localhost/OSPS'  # Centralized connection string

    @staticmethod
    def create_report(report_type):
        if report_type.lower() == "user":
            return UserReport(ReportFactory.connection_string)
        elif report_type.lower() == "management":
            return ManagementReport(ReportFactory.connection_string)
        else:
            raise ValueError(f"Unknown report type: {report_type}")

    @staticmethod
    def generate_and_print_report(report_type, user_id=None):
        report = ReportFactory.create_report(report_type)
        if report_type.lower() == "user" and user_id is not None:
            report.print_report(user_id)
        else:
            report.print_report()
