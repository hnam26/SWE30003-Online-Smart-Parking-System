CREATE DATABASE OSPS;

USE OSPS;

CREATE TABLE User (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    username VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(10) NOT NULL,
    password CHAR(60) NOT NULL
);

CREATE TABLE Vehicle (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    license_plate VARCHAR(20) UNIQUE NOT NULL,
    vehicle_type VARCHAR(50) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE ParkingLot (
    parking_lot_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    location VARCHAR(100) NOT NULL
);

CREATE TABLE ParkingSlot (
    parking_slot_id INT AUTO_INCREMENT PRIMARY KEY,
    parking_lot_id INT NOT NULL,
    slot_number VARCHAR(10) NOT NULL,
    is_available BOOLEAN NOT NULL,
    FOREIGN KEY (parking_lot_id) REFERENCES ParkingLot(parking_lot_id)
);

CREATE TABLE Booking (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    vehicle_id INT NOT NULL,
    parking_slot_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    duration DECIMAL(2, 1) NOT NULL,
    status ENUM('PENDING', 'PAID', 'IN', 'OUT', 'CANCELLED') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (vehicle_id) REFERENCES Vehicle(vehicle_id),
    FOREIGN KEY (parking_slot_id) REFERENCES ParkingSlot(parking_slot_id)
);

CREATE TABLE Payment (
    payment_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT NOT NULL UNIQUE,
    user_id INT NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (booking_id) REFERENCES Booking(booking_id)
);

CREATE TABLE Invoice (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    payment_id INT NOT NULL UNIQUE,
    issue_date DATETIME NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (payment_id) REFERENCES Payment(payment_id)
);

CREATE TABLE ReportType (
    report_type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(50) NOT NULL
);

CREATE TABLE Report (
    report_id INT AUTO_INCREMENT PRIMARY KEY,
    report_type INT NOT NULL,
    generated_date DATETIME NOT NULL,
    details TEXT,
    FOREIGN KEY (report_type) REFERENCES ReportType(report_type_id)
);

SELECT * FROM User;