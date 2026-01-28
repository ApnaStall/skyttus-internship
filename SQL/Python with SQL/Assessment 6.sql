USE skyttus_internship;
GO

-- ACCOUNTS TABLE
CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    account_name VARCHAR(50),
    balance INT
);
GO

-- INITIAL DATA
INSERT INTO accounts VALUES
(1, 'Amit', 5000),
(2, 'Rohit', 3000);
GO

/*
   START A TRANSACTION
   INSERT RECORD
   ROLLBACK CHANGES
*/
BEGIN TRANSACTION;

INSERT INTO accounts VALUES
(3, 'Sneha', 4000);

-- Check data before rollback
SELECT * FROM accounts;

ROLLBACK;

-- Data after rollback
SELECT * FROM accounts;
GO

-- COMMIT VALID TRANSACTION
BEGIN TRANSACTION;

INSERT INTO accounts VALUES
(3, 'Sneha', 4000);

COMMIT;

-- Data after commit
SELECT * FROM accounts;
GO

/*
   MONEY TRANSFER USING TRANSACTION
   Transfer 1000 from Amit to Rohit
*/
BEGIN TRANSACTION;

-- Deduct from Amit
UPDATE accounts
SET balance = balance - 1000
WHERE account_name = 'Amit';

-- Add to Rohit
UPDATE accounts
SET balance = balance + 1000
WHERE account_name = 'Rohit';

-- Check balances before commit
SELECT * FROM accounts;

COMMIT;

-- Final balances
SELECT * FROM accounts;
GO
