USE skyttus_internship;
GO

-- TABLE CREATION
CREATE TABLE employees_adv (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    salary INT,
    hire_date DATE
);
GO

CREATE TABLE employees_backup (
    emp_id INT PRIMARY KEY
);
GO

-- SAMPLE DATA
INSERT INTO employees_adv VALUES
(1, 'Amit', 60000, '2024-01-01'),
(2, 'Rohit', 55000, '2023-12-10'),
(3, 'Sneha', 40000, '2023-08-15'),
(4, 'Priya', 70000, '2024-03-20'),
(5, 'Karan', 45000, '2023-11-05'),
(6, 'Neha', 52000, '2024-02-01'),
(7, 'Amit', 60000, '2024-01-01'); -- duplicate record
GO

INSERT INTO employees_backup VALUES (1), (2), (4);
GO

-- FIND Nth HIGHEST SALARY
DECLARE @N INT = 2;

SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees_adv
) t
WHERE rnk = @N;
GO

-- REMOVE DUPLICATE RECORDS
WITH cte AS (
    SELECT *,
           ROW_NUMBER() OVER (
               PARTITION BY emp_name, salary, hire_date
               ORDER BY emp_id
           ) AS rn
    FROM employees_adv
)
DELETE FROM cte
WHERE rn > 1;
GO

-- FIND RECORDS COMMON IN TWO TABLES
SELECT e.*
FROM employees_adv e
INNER JOIN employees_backup b
ON e.emp_id = b.emp_id;
GO

-- EMPLOYEES HIRED IN LAST 6 MONTHS
SELECT *
FROM employees_adv
WHERE hire_date >= DATEADD(MONTH, -6, GETDATE());
GO

-- FIND CONTINUOUS DUPLICATE VALUES
SELECT DISTINCT e1.salary
FROM employees_adv e1
JOIN employees_adv e2
ON e1.emp_id = e2.emp_id - 1
WHERE e1.salary = e2.salary;
GO
