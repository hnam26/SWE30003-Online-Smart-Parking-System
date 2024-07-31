from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Boolean, DateTime, DECIMAL, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import threading
import sqlalchemy
from datetime import datetime
from tabulate import tabulate

Base = sqlalchemy.orm.declarative_base()

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(10), nullable=False)
    password = Column(String(100), nullable=False)
    vehicles = relationship('Vehicle', back_populates='user')
    bookings = relationship('Booking', back_populates='user')

class Vehicle(Base):
    __tablename__ = 'Vehicle'
    vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    license_plate = Column(String(20), unique=True, nullable=False)
    vehicle_type = Column(String(50), nullable=False)
    user = relationship('User', back_populates='vehicles')
    bookings = relationship('Booking', back_populates='vehicle')

class ParkingLot(Base):
    __tablename__ = 'ParkingLot'
    parking_lot_id = Column(Integer, primary_key=True, autoincrement=True)
    location = Column(String(100), nullable=False)
    slots = relationship('ParkingSlot', back_populates='parking_lot')

class ParkingSlot(Base):
    __tablename__ = 'ParkingSlot'
    parking_slot_id = Column(Integer, primary_key=True, autoincrement=True)
    parking_lot_id = Column(Integer, ForeignKey('ParkingLot.parking_lot_id'), nullable=False)
    slot_number = Column(String(10), nullable=False)
    is_available = Column(Boolean, nullable=False)
    parking_lot = relationship('ParkingLot', back_populates='slots')
    bookings = relationship('Booking', back_populates='parking_slot')

class Booking(Base):
    __tablename__ = 'Booking'
    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('Vehicle.vehicle_id'), nullable=False)
    parking_slot_id = Column(Integer, ForeignKey('ParkingSlot.parking_slot_id'), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    user = relationship('User', back_populates='bookings')
    vehicle = relationship('Vehicle', back_populates='bookings')
    parking_slot = relationship('ParkingSlot', back_populates='bookings')
    payment = relationship('Payment', uselist=False, back_populates='booking')

class Payment(Base):
    __tablename__ = 'Payment'
    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey('Booking.booking_id'), nullable=False, unique=True)
    payment_method = Column(String(50), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    booking = relationship('Booking', back_populates='payment')
    invoice = relationship('Invoice', uselist=False, back_populates='payment')

class Invoice(Base):
    __tablename__ = 'Invoice'
    invoice_id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey('Payment.payment_id'), nullable=False, unique=True)
    issue_date = Column(DateTime, nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    payment = relationship('Payment', back_populates='invoice')

class ReportType(Base):
    __tablename__ = 'ReportType'
    report_type_id = Column(Integer, primary_key=True, autoincrement=True)
    type_name = Column(String(50), nullable=False)
    reports = relationship('Report', back_populates='report_type')

class Report(Base):
    __tablename__ = 'Report'
    report_id = Column(Integer, primary_key=True, autoincrement=True)
    report_type_id = Column(Integer, ForeignKey('ReportType.report_type_id'), nullable=False)
    generated_date = Column(DateTime, nullable=False)
    details = Column(String)
    report_type = relationship('ReportType', back_populates='reports')

class DatabaseAccess:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, connection_string):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseAccess, cls).__new__(cls)
                cls._instance.engine = create_engine(connection_string)
                cls._instance.Session = sessionmaker(bind=cls._instance.engine)
                Base.metadata.create_all(cls._instance.engine)
                print("Database connection established")
            return cls._instance

    def getSession(self):
        return self.Session()

    def close(self):
        if self._instance and self._instance.engine:
            self._instance.engine.dispose()
            print("Database connection closed")
    
    def registerUser(self):
        session = self.getSession()
        try:
            name = input("Enter your name: ")
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            phone = input("Enter your phone number: ")
            password = input("Enter your password: ")

            newUser = User(name=name, username=username, email=email, phone=phone, password=password)
            session.add(newUser)
            session.commit()
            print("User registered successfully!")
            self.queryMenu()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")
        finally:
            session.close()
    
    def loginUser(self):
        session = self.getSession()
        try:
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")

            user = session.query(User).filter_by(username=username, email=email, password=password).first()
            if user:
                print("Login successful!")
                self.queryMenu()
            else:
                print("Login failed: Invalid credentials.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()

    def queryMenu(self):
        session = self.getSession()
        try:
            while True:
                print("\nQuery Menu:")
                print("1. Execute a SQL query")
                print("2. Logout")
                choice = input("Enter your choice: ")

                if choice == '1':
                    self.queryDatabase(session)
                elif choice == '2':
                    break
                else:
                    print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()

    def queryDatabase(self, session):
        try:
            sqlQuery = input("Enter your SQL query: ")
            result = session.execute(text(sqlQuery))
            columns = result.keys()
            rows = []
            for row in result:
                formattedRow = [value.strftime("%Y-%m-%d %H:%M:%S") if isinstance(value, datetime) else value for value in row]
                rows.append(formattedRow)
            print(tabulate(rows, headers=columns, tablefmt="grid"))
        except Exception as e:
            print(f"An error occurred while executing the query: {e}")

def main():
    connectionString = 'mysql+mysqlconnector://root:12345@localhost/OSPS'
    db = DatabaseAccess(connectionString)
    
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            db.registerUser()
        elif choice == '2':
            db.loginUser()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    db.close()
