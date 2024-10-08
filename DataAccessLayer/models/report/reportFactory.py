from DataAccessLayer.models.report.userReport import UserReport
from DataAccessLayer.models.report.managementReport import ManagementReport

class ReportFactory:
    @staticmethod
    def getReport(reportType: str):
        if reportType == 'user':
            return UserReport()
        elif reportType == 'management':
            return ManagementReport()
        else:
            raise ValueError(f"Unknown report type: {reportType}")

    def reportMenu(self, userId: int):
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
                    case '2':
                        reportType = 'management'
                        userId = None  
                    case '3':
                        break
                    case _:
                        print("Invalid choice. Please try again.")
                        break

                report = ReportFactory.getReport(reportType)
                if reportType == 'user':
                    report.printReport(userId)
                else:
                    report.printReport()
            except ValueError as e:
                print(e)
