USE e_commerce;
GO

-- Add index to improve search on orders.customer_id
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);
GO

-- Analyze query performance
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
GO

SELECT 
    o.order_id,
    o.order_date,
    o.amount,
    c.name,
    c.city
FROM orders o
INNER JOIN customers c
ON o.customer_id = c.customer_id;
GO

SET STATISTICS IO OFF;
SET STATISTICS TIME OFF;
GO

-- Optimized JOIN query
SELECT 
    o.order_id,
    o.order_date,
    o.amount,
    c.name,
    c.city
FROM orders o
INNER JOIN customers c
ON o.customer_id = c.customer_id;
GO
