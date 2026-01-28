USE skyttus_internship;
GO

-- USERS TABLE
CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,   -- Primary Key
    name VARCHAR(50),
    email VARCHAR(100) UNIQUE,               -- Unique Email
    password VARCHAR(100) NOT NULL           -- NOT NULL Password
);
GO

-- ORDERS TABLE
CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT,
    order_date DATE,
    amount INT
);
GO

-- ADD FOREIGN KEY BETWEEN orders AND users
ALTER TABLE orders
ADD CONSTRAINT fk_orders_users
FOREIGN KEY (user_id)
REFERENCES users(user_id);
GO

-- CREATE INDEX ON email COLUMN
CREATE INDEX idx_users_email
ON users(email);
GO

-- SAMPLE DATA
INSERT INTO users (name, email, password) VALUES
('Amit', 'amit@gmail.com', 'pass123'),
('Rohit', 'rohit@gmail.com', 'pass456'),
('Sneha', 'sneha@gmail.com', 'pass789');
GO

INSERT INTO orders (user_id, order_date, amount) VALUES
(1, '2024-01-01', 2000),
(1, '2024-01-10', 1500),
(2, '2024-01-05', 3000),
(3, '2024-01-12', 4000);
GO

-- CREATE VIEW: User Order Summary
CREATE VIEW user_order_summary AS
SELECT
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.amount) AS total_amount
FROM users u
LEFT JOIN orders o
ON u.user_id = o.user_id
GROUP BY
    u.user_id,
    u.name,
    u.email;
GO

-- VIEW OUTPUT
SELECT * FROM user_order_summary;
GO
