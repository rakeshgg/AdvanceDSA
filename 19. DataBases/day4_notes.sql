-- SQL Filters and Problems
-- Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.

-- 1- write a sql to get all the orders where customers name has "a" as second character and "d" as fourth character (58 rows)
select * from orders where customer_name like '_a_d%';

-- 2- write a sql to get all the orders placed in the month of dec 2020 (352 rows) 
select * from orders where  order_date between '2020-12-01' and '2020-12-31';

-- 3- write a query to get all the orders where ship_mode is neither in 'Standard Class' nor in 'First Class' and ship_date is after nov 2020 (944 rows)
select * from orders where  ship_mode not in ('Standard Class','First Class')
and ship_date > '2020-11-30'

-- 4- write a query to get all the orders where customer name neither start with "A" and nor ends with "n" (9815 rows)
select * from orders where customer_name not like 'A%n';

-- 5- write a query to get all the orders where profit is negative (1871 rows)
select * from orders where profit<0

-- 6- write a query to get all the orders where either quantity is less than 3 or profit is 0 (3348)
select * from orders where profit=0 or quantity<3

-- 7- your manager handles the sales for South region and he wants you to create a report of all the orders in his region where some discount is provided to the customers (815 rows)
select * from orders where region='South' and discount>0

-- 8- write a query to find top 5 orders with highest sales in furniture category
-- order of execution - from go to order table , where filter and select * and do order by and apply -- top 5
-- from , where, select *, oder by than apply top 5
select top 5 * from orders where category='Furniture' order by sales desc 


-- 9- write a query to find all the records in technology and furniture category for the orders placed in the year 2020 only (1021 rows)
select   * from orders where category in ('Furniture','Technology') 
and order_date between '2020-01-01' and '2020-12-31'


-- 10-write a query to find all the orders where order date is in year 2020 but ship date is in 2021 (33 rows)
select   * from orders where 
order_date between '2020-01-01' and '2020-12-31' and ship_date between '2021-01-01' and '2021-12-31'
