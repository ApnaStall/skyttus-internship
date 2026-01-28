-- DATABASE CREATION
CREATE DATABASE SkyttusDB;
GO

USE skyttus_internship;
GO

-- TABLE CREATION
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);
GO

-- SAMPLE DATA
INSERT INTO students VALUES
(1, 'Amit',   'CSE', 2, 85),
(2, 'Rohit',  'ECE', 3, 72),
(3, 'Sneha',  'CSE', 1, 90),
(4, 'Priya',  'IT',  4, 78),
(5, 'Karan',  'CSE', 2, 65),
(6, 'Neha',   'ECE', 3, 88);
GO

-- Display all student records
SELECT * 
FROM students;
GO

-- Display only name and department
SELECT name, department
FROM students;
GO

-- Students with marks > 75
SELECT *
FROM students
WHERE marks > 75;
GO

-- Students from CSE department
SELECT *
FROM students
WHERE department = 'CSE';
GO

-- Sort students by marks (descending)
SELECT *
FROM students
ORDER BY marks DESC;
GO

-- Display top 3 scorers
SELECT TOP 3 *
FROM students
ORDER BY marks DESC;
GO
