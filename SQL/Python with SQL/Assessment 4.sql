USE company_db;
GO

-- Employees earning more than average salary
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);
GO

-- Department with highest total salary
SELECT TOP 1
    d.dept_name,
    SUM(e.salary) AS Total_Salary
FROM employees e
INNER JOIN departments d
ON e.dept_id = d.dept_id
GROUP BY d.dept_name
ORDER BY SUM(e.salary) DESC;
GO

-- Employee with second highest salary
SELECT TOP 1 *
FROM employees
WHERE salary < (
    SELECT MAX(salary)
    FROM employees
)
ORDER BY salary DESC;
GO

-- Employees working in same department as "Amit"
SELECT *
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);
GO
