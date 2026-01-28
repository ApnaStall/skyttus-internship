-- DATABASE CREATION
CREATE DATABASE mess_management;
GO

USE mess_management;
GO

-- TABLES CREATION
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    room_no INT
);

CREATE TABLE staff (
    staff_id INT PRIMARY KEY,
    name VARCHAR(50),
    role VARCHAR(30)
);

CREATE TABLE meals (
    meal_id INT PRIMARY KEY,
    meal_type VARCHAR(20),
    price INT
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY,
    student_id INT,
    meal_id INT,
    meal_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    student_id INT,
    amount INT,
    payment_date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);
GO

-- SAMPLE DATA
INSERT INTO students VALUES
(1, 'Amit', 101),
(2, 'Rohit', 102),
(3, 'Sneha', 103),
(4, 'Priya', 104);

INSERT INTO staff VALUES
(1, 'Ramesh', 'Cook'),
(2, 'Suresh', 'Cleaner');

INSERT INTO meals VALUES
(1, 'Breakfast', 50),
(2, 'Lunch', 80),
(3, 'Dinner', 70);

INSERT INTO attendance VALUES
(1, 1, 1, '2024-03-01'),
(2, 1, 2, '2024-03-01'),
(3, 2, 2, '2024-03-01'),
(4, 3, 3, '2024-03-01'),
(5, 1, 3, '2024-03-02'),
(6, 4, 2, '2024-03-02');

INSERT INTO payments VALUES
(1, 1, 3000, '2024-03-01'),
(2, 2, 2500, '2024-03-01'),
(3, 3, 2000, '2024-03-01');
GO

-- 15 BUSINESS QUERIES

-- 1. All students
SELECT * FROM students;
GO

-- 2. Students who attended lunch
SELECT DISTINCT s.name
FROM students s
JOIN attendance a ON s.student_id = a.student_id
JOIN meals m ON a.meal_id = m.meal_id
WHERE m.meal_type = 'Lunch';
GO

-- 3. Total meals taken by each student
SELECT student_id, COUNT(*) AS total_meals
FROM attendance
GROUP BY student_id;
GO

-- 4. Total payment collected
SELECT SUM(amount) AS total_collection
FROM payments;
GO

-- 5. Students who never attended meals
SELECT s.name
FROM students s
LEFT JOIN attendance a ON s.student_id = a.student_id
WHERE a.attendance_id IS NULL;
GO

-- 6. Meal-wise attendance count
SELECT m.meal_type, COUNT(a.attendance_id) AS total_attendance
FROM meals m
LEFT JOIN attendance a ON m.meal_id = a.meal_id
GROUP BY m.meal_type;
GO

-- 7. Students who attended dinner
SELECT DISTINCT s.name
FROM students s
JOIN attendance a ON s.student_id = a.student_id
JOIN meals m ON a.meal_id = m.meal_id
WHERE m.meal_type = 'Dinner';
GO

-- 8. Daily attendance report
SELECT meal_date, COUNT(*) AS total_students
FROM attendance
GROUP BY meal_date;
GO

-- 9. Students who paid more than 2500
SELECT s.name, p.amount
FROM students s
JOIN payments p ON s.student_id = p.student_id
WHERE p.amount > 2500;
GO

-- 10. Total meal cost per student
SELECT s.name, SUM(m.price) AS total_cost
FROM students s
JOIN attendance a ON s.student_id = a.student_id
JOIN meals m ON a.meal_id = m.meal_id
GROUP BY s.name;
GO

-- 11. Most consumed meal
SELECT TOP 1 m.meal_type, COUNT(*) AS count
FROM attendance a
JOIN meals m ON a.meal_id = m.meal_id
GROUP BY m.meal_type
ORDER BY COUNT(*) DESC;
GO

-- 12. Students with more than 2 meals
SELECT student_id
FROM attendance
GROUP BY student_id
HAVING COUNT(*) > 2;
GO

-- 13. Students without payment
SELECT s.name
FROM students s
LEFT JOIN payments p ON s.student_id = p.student_id
WHERE p.payment_id IS NULL;
GO

-- 14. Monthly payment summary
SELECT MONTH(payment_date) AS month, SUM(amount) AS total
FROM payments
GROUP BY MONTH(payment_date);
GO

-- 15. Student with highest meal expense
SELECT TOP 1 s.name, SUM(m.price) AS expense
FROM students s
JOIN attendance a ON s.student_id = a.student_id
JOIN meals m ON a.meal_id = m.meal_id
GROUP BY s.name
ORDER BY SUM(m.price) DESC;
GO

-- QUERY OPTIMIZATION

CREATE INDEX idx_attendance_student ON attendance(student_id);
CREATE INDEX idx_attendance_meal ON attendance(meal_id);
CREATE INDEX idx_payments_student ON payments(student_id);
GO
