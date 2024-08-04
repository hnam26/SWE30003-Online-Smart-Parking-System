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
                        userId = None  
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
