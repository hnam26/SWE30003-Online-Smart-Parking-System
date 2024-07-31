import BusinessLogic
from DataAccessLayer.database.databaseAccess import DatabaseAccess
from DataAccessLayer.report.reportFactory import ReportFactory

def main():
    # Database connection string
    connection_string = 'mysql+mysqlconnector://root:*Sinh08062004*@localhost/OSPS'
    
    # Đây là 2 phần code của report để em test thử nó chạy được chưa, 
    # khi mà mình có option để chọn print report thì có thể bỏ đoạn này vào.
    
    # Initialize the ReportFactory with the database connection
    ReportFactory.initialize_database(connection_string)
    
    # Run the report generation process
    ReportFactory.run_report_generation()
    
    # Initialize DatabaseAccess
    db_access = DatabaseAccess(connection_string)
    
    # Create a session to interact with the database
    session = db_access.getSession()
    db_access.queryMenu()
    
    # Close the session
    session.close()

if __name__ == "__main__":
    main()
