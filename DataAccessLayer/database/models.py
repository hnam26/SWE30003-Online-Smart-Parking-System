# from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Date, DECIMAL
# from sqlalchemy.orm import relationship, declarative_base
#
# Base = declarative_base()

# class UserTable(Base):
#     __tablename__ = 'User'
#     user_id = Column(Integer, primary_key=True, autoincrement=True)
#     username = Column(String(100), nullable=False)
#     password = Column(String(100), nullable=False)
#     first_name = Column(String(100), nullable=False)
#     last_name = Column(String(100), nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     phone = Column(String(10), nullable=False)
#     dob = Column(Date, nullable=False)
#     vehicles = relationship('VehicleTable', back_populates='user')
#     bookings = relationship('BookingTable', back_populates='user')
#     payments = relationship('PaymentTable', back_populates='user')
#
# class VehicleTable(Base):
#     __tablename__ = 'Vehicle'
#     vehicle_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
#     license_plate = Column(String(20), unique=True, nullable=False)
#     vehicle_type = Column(String(50), nullable=False)
#     user = relationship('UserTable', back_populates='vehicles')
#     bookings = relationship('BookingTable', back_populates='vehicle')
#
# class ParkingLotTable(Base):
#     __tablename__ = 'ParkingLot'
#     parking_lot_id = Column(Integer, primary_key=True, autoincrement=True)
#     location = Column(String(100), nullable=False)
#     slots = relationship('ParkingSlotTable', back_populates='parking_lot')
#
# class ParkingSlotTable(Base):
#     __tablename__ = 'ParkingSlot'
#     parking_slot_id = Column(Integer, primary_key=True, autoincrement=True)
#     parking_lot_id = Column(Integer, ForeignKey('ParkingLot.parking_lot_id'), nullable=False)
#     slot_number = Column(String(10), nullable=False)
#     is_available = Column(Boolean, nullable=False)
#     parking_lot = relationship('ParkingLotTable', back_populates='slots')
#     bookings = relationship('BookingTable', back_populates='parking_slot')
#
# class BookingTable(Base):
#     __tablename__ = 'Booking'
#     booking_id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
#     vehicle_id = Column(Integer, ForeignKey('Vehicle.vehicle_id'), nullable=False)
#     parking_slot_id = Column(Integer, ForeignKey('ParkingSlot.parking_slot_id'), nullable=False)
#     start_time = Column(DateTime, nullable=False)
#     duration = Column(DECIMAL(2, 1), nullable=False)
#     user = relationship('UserTable', back_populates='bookings')
#     vehicle = relationship('VehicleTable', back_populates='bookings')
#     parking_slot = relationship('ParkingSlotTable', back_populates='bookings')
#     payment = relationship('PaymentTable', uselist=False, back_populates='booking')
#
# class PaymentTable(Base):
#     __tablename__ = 'Payment'
#     payment_id = Column(Integer, primary_key=True, autoincrement=True)
#     booking_id = Column(Integer, ForeignKey('Booking.booking_id'), nullable=False, unique=True)
#     user_id = Column(Integer, ForeignKey('User.user_id'), nullable=False)
#     payment_method = Column(String(50), nullable=False)
#     amount = Column(DECIMAL(10, 2), nullable=False)
#     payment_date = Column(DateTime, nullable=False)
#     user = relationship('UserTable', back_populates='payments')
#     booking = relationship('BookingTable', back_populates='payment')
#     invoice = relationship('InvoiceTable', uselist=False, back_populates='payment')
#
# class InvoiceTable(Base):
#     __tablename__ = 'Invoice'
#     invoice_id = Column(Integer, primary_key=True, autoincrement=True)
#     payment_id = Column(Integer, ForeignKey('Payment.payment_id'), nullable=False, unique=True)
#     issue_date = Column(DateTime, nullable=False)
#     amount = Column(DECIMAL(10, 2), nullable=False)
#     payment = relationship('PaymentTable', back_populates='invoice')
#
# class ReportTypeTable(Base):
#     __tablename__ = 'ReportType'
#     report_type_id = Column(Integer, primary_key=True, autoincrement=True)
#     type_name = Column(String(50), nullable=False)
#     reports = relationship('ReportTable', back_populates='report_type')
#
# class ReportTable(Base):
#     __tablename__ = 'Report'
#     report_id = Column(Integer, primary_key=True, autoincrement=True)
#     report_type_id = Column(Integer, ForeignKey('ReportType.report_type_id'), nullable=False)
#     generated_date = Column(DateTime, nullable=False)
#     details = Column(String)
#     report_type = relationship('ReportTypeTable', back_populates='reports')
