-- DATABASE CREATION
CREATE DATABASE e_commerce;
GO

USE e_commerce;
GO

-- TABLES CREATION
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50)
);
GO

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    price INT
);
GO

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount INT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
GO

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
GO

-- SAMPLE DATA
INSERT INTO customers VALUES
(1, 'Amit', 'Delhi'),
(2, 'Rohit', 'Mumbai'),
(3, 'Sneha', 'Pune'),
(4, 'Priya', 'Delhi');
GO

INSERT INTO products VALUES
(1, 'Laptop', 50000),
(2, 'Mobile', 20000),
(3, 'Headphones', 3000);
GO

INSERT INTO orders VALUES
(101, 1, '2024-01-10', 70000),
(102, 2, '2024-02-15', 20000),
(103, 1, '2024-03-05', 50000),
(104, 3, '2024-03-20', 3000);
GO

INSERT INTO order_items VALUES
(101, 1, 1),
(101, 2, 1),
(102, 2, 1),
(103, 1, 1),
(104, 3, 1);
GO

-- Total orders per customer
SELECT 
    c.name,
    COUNT(o.order_id) AS Total_Orders
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.name;
GO

-- Customers who never placed an order
SELECT c.name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
GO

-- Highest selling product
SELECT TOP 1
    p.product_name,
    SUM(oi.quantity) AS Total_Quantity
FROM order_items oi
INNER JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY SUM(oi.quantity) DESC;
GO

-- Monthly sales report
SELECT 
    YEAR(order_date) AS Year,
    MONTH(order_date) AS Month,
    SUM(amount) AS Total_Sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY Year, Month;
GO

-- Customers with total purchase > ₹50,000
SELECT 
    c.name,
    SUM(o.amount) AS Total_Purchase
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.name
HAVING SUM(o.amount) > 50000;
GO

-- Top 3 cities by revenue
SELECT TOP 3
    c.city,
    SUM(o.amount) AS Total_Revenue
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY SUM(o.amount) DESC;
GO
