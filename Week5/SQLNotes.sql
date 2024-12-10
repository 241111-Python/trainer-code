-- This is a SQL Comment!

-- Atomic - each value is held alone
-- Consistent - the same request twice should give the same result
-- Isolated - a transaction (set of functionality) will not interfere with another running operation
-- Durable - the data should persist when the system restarts

-- Normalization - The normal float8_var_samp
    -- the pattern or rules that we're using to define our data
    -- 1NF - The Key - every entry must have a unique key (primary key)
    -- 2ND - The Whole Key - every value for an entry should be dependant on the key
    -- 3NF - Nothing But The Key - A value must be dependant on the WHOLE primary key (mostly a composit key thing)


-- SQL Sublanguages "Families"
    -- DDL - Data Definition Language - Create, Alter, Drop - Managing the structure of the data (the tables)
    -- DML - Data Manipulation Language - Insert, Update, Delete - Managing the entries of the tables (the values)
    -- DQL - Data Query Language - Select, From, Where - Retrieving values/entries from the tables (the queries)
    -- DCL - Data Control Language - Revoke, Grant - Managing the access to the database
    -- TCL - Transaction Control Language - Groups a set of executing commands into a "bundle"/a transaction. 

/*
This is a multi-line comment in SQL!
*/

-- DQL
-- SELECT ALWAYS return a table
SELECT 2;
-- and it can do things OTHER than just getting data back from a table!
SELECT 2 + 2;
-- ; to end a query/thought
-- SQL is NOT keyword-case sensitive, but using uppercase for keywords is a common convention
select 6;
SELECT 'This is a string!'; -- Single-quotation mark stings!

-- SELECT - return a response
-- (what are we looking for)
-- FROM - tell the DB where to look for the info we want to return!

SELECT * FROM film;
-- SELECT * FROM [postgres].[film]; -- the bracket notation is also pretty common

SELECT film_id, title FROM film;
SELECT film_id, title, rental_duration FROM film WHERE rental_duration = 5;

SELECT film_id, title, rental_duration 
    FROM film 
    WHERE rental_duration = 5 
        OR rental_duration = 6;

SELECT title || ' ' || description AS Title_Desc, rental_duration -- we can use AS to alias a column
    FROM film 
    WHERE rental_duration = 5 
        OR rental_duration = 6;

-- Aggregate Functions - accepts some parameters, and returns a Scalar (a single value)
    -- COUNT, SUM, MIN, MAX

SELECT * FROM invoice;

SELECT COUNT(*) FROM invoice; -- The count of the number of entries in the table
SELECT SUM(total) FROM invoice; -- the Sum of the total column
SELECT MIN(total) FROM invoice;
SELECT MAX(total) FROM invoice;

SELECT customer_id, total 
    FROM invoice
    ORDER BY customer_id; -- we can use ORDER By to sort the data

SELECT customer_id, SUM(total) AS customer_total
    FROM invoice
    GROUP BY customer_id
    ORDER BY customer_id; -- using GROUP BY to group the customer ids together to run the SUM AGGREGATE

-- HAVING will give us another way to filter values as a condition on GROUP BY
SELECT customer_id, SUM(total) AS customer_total    -- return a table with the two columns 'customer_id' and the sum of the values of the 'total' column, but call it 'customer_total'
    FROM invoice                                    -- search the 'invoice' table for the data 
    WHERE billing_country = 'USA'                   -- only return values that have a 'billing-country' equal to 'USA'
    GROUP BY customer_id                            -- combine all entries/instances that have the same 'customer_id' values...
    HAVING SUM(total) > 40                          -- calculate the sum of the 'total' column for each group of 'customer_id', and only return values that are greater than 40
    ORDER BY customer_id;                           -- sort any matching entries/groups based on the 'customer_id'

-- Order of Execution 
-- FROM
-- WHERE
-- GROUP BY
-- HAVING
-- SELECT
-- ORDER BY