# from vehicle import Vehicle
# from utils.typesOfVehicle import TypesOfVehicle
from DataAccessLayer.report.reportFactory import ReportFactory  # Import the ReportFactory

def main():
    # Create a car with 4 seats
    # car1 = Vehicle("1234", TypesOfVehicle.fourSeats)
    # print(car1)
    # Create a car with 7 seats
    # car2 = Vehicle("5678", TypesOfVehicle.sevenSeats)
    # print(car2)
    
    # Get the user ID from the user input
    user_id = int(input("Enter the user ID for the user report: "))

    # Generate and print user report
    print("User Report:")
    ReportFactory.generate_and_print_report("user", user_id)

    # Generate and print management report
    print("Management Report:")
    ReportFactory.generate_and_print_report("management")

if __name__ == "__main__":
    main()
