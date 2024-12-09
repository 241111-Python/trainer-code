# Chinook Challenge Questions

## On the Chinook DB, practice writing queries with the following exercises

### Basic Queries

- List all customers (full name, customer id, and country) who are not in the USA

- List all customers from Brazil

- List all sales agents

- Retrieve a list of all countries in billing addresses on invoices

- Retrieve how many invoices there were in 2009, and what was the sales total for that year?
  - (Challenge: find the invoice count sales total for every year using one query)

- How many line items were there for invoice #37

- How many invoices per country?

- Retrieve the total sales per country, ordered by the highest total sales first.

### Joins

- Show all invoices of customers from brazil (mailing address not billing)

- Show all invoices together with the name of the sales agent for each one

- Show all playlists ordered by the total number of tracks they have

- Which sales agent made the most sales in 2009?

- How many customers are assigned to each sales agent?

- Which track was purchased the most ing 20010?

- Show the top three best selling artists.

- Which customers have the same initials as at least one other customer?

### Advanced Queries

Solve these with a mixture of joins, sub-queries, CTE, and set operators. Solve at least one of them in two different ways, and see if the execution plan for them is the same, or different.

- 1. Which artists did not make any albums at all?

- 2. Which artists did not record any tracks of the Latin genre?

- 3. Which video track has the longest length? (use media type table)

- 4. Find the names of the customers who live in the same city as the boss employee (the one who reports to nobody.)

- 5. How many audio tracks were bought by German customers, and what was the total price paid for them?

- 6. List the names and countries of the customers supported by an employee who was hired younger than 35.

### DML exercises

1. insert two new records into the employee table.

2. insert two new records into the tracks table.

3. update customer Aaron Mitchell's name to Robert Walter

4. delete one of the employees you inserted.

5. delete customer Robert Walter.
