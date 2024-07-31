from vehicle import Vehicle
from DataAccessLayer.utils.typesOfVehicle import TypesOfVehicle
from user import User


def main():
    # Create a car with 4 seats
    car1 = Vehicle("1234", TypesOfVehicle.fourSeats)
    print(car1)
    # Create a car with 7 seats
    car2 = Vehicle("5678", TypesOfVehicle.sevenSeats)
    print(car2)
    
    # user = User("username", "password", "firstName", "lastName", "email", "phone", "dob")

    # print(user._firstName)


if __name__ == "__main__":
    main()
