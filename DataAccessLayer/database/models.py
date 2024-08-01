from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Date, DECIMAL
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(10), nullable=False)
    dob = Column(Date, nullable=False)
    vehicles = relationship('Vehicle', back_populates='personal')
    bookings = relationship('Booking', back_populates='personal')
    payments = relationship('Payment', back_populates='personal')

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
    duration = Column(DECIMAL(2, 1), nullable=False)
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
    user = relationship('User', back_populates='payments')
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
