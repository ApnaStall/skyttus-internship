-- DATABASE CREATION
CREATE DATABASE company_db;
GO

USE company_db;
GO

-- TABLES CREATION
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);
GO

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);
GO

-- SAMPLE DATA
INSERT INTO departments VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');
GO

INSERT INTO employees VALUES
(101, 'Amit',  2, 60000),
(102, 'Rohit', 2, 55000),
(103, 'Sneha', 1, 40000),
(104, 'Priya', 3, 70000),
(105, 'Karan', 2, 45000),
(106, 'Neha',  NULL, 52000);
GO

-- Employee name with department name
SELECT 
    e.emp_name,
    d.dept_name
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id;
GO

-- Employees earning more than 50,000
SELECT *
FROM employees
WHERE salary > 50000;
GO

-- Department-wise total salary
SELECT 
    d.dept_name,
    SUM(e.salary) AS Total_Salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name;
GO

-- Departments with more than 2 employees
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS Employee_Count
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;
GO

-- Employees without a department
SELECT *
FROM employees
WHERE dept_id IS NULL;
GO
