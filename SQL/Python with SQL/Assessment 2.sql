USE skyttus_internship;
GO

-- Count total number of students
SELECT COUNT(*) AS Total_Students
FROM students;
GO

-- Find average marks of students
SELECT AVG(marks) AS Average_Marks
FROM students;
GO

-- Find highest and lowest marks
SELECT 
    MAX(marks) AS Highest_Marks,
    MIN(marks) AS Lowest_Marks
FROM students;
GO

-- Department-wise average marks
SELECT 
    department,
    AVG(marks) AS Average_Marks
FROM students
GROUP BY department;
GO
-- Departments where average marks > 70
SELECT 
    department,
    AVG(marks) AS Average_Marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;
GO
