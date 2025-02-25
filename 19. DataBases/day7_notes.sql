-- 6. SQL functions - date and string functions, case when
select * from employee;
select * from dept;
-- emp_id, manager_id refering to employee id of same table - so use self join
-- self join -- join table with itself
-- Employee name, manager name of each employee
/* Intresting concepts - both same table for self joins
   split table in two say emp1, emp2
   than for which col we should join
   join emp1 - maneger_id with emp2 - emp_id
   emp1.manager_id = emp2.emp_id
   join fk to pk of that table
*/
select e1.emp_id, e1.emp_name, e2.emp_name as manager_name 
from employee as e1
inner join employee as e2 on e1.manager_id = e2.emp_id;

select e1.emp_id, e1.emp_name, e2.emp_name as manager_name 
from employee as e1
inner join employee as e2 on e1.manager_id = e2.emp_id
where e1.salary > e2.salary;
-- e1.salary is Employee Salary
-- e2.salary is Manager Salary

-- min, max, avg, count() these are functions all 4 works on integer, decimal,-  date, string only min, max works
-- print all empy name of each departemnts , dep_id, list_of_employyess, 1, ankit, mohit, vikas - this is also kind of agregation
-- aggregating all values of columns name, listing all values -- STRING_AGG(emp_name, seperator)
select dept_id, STRING_AGG(emp_name, ',') as list_of_employees
from employee
group by dept_id;

--- STRING_AGG want to sort
select dept_id, STRING_AGG(emp_name, ',') WITHIN GROUP (ORDER BY  salary desc) as list_of_employees
from employee
group by dept_id;


--- Date Functions -- datepart(year, field_name)
-- year of date -- year is integer data type so fast comapre to string

select Order_ID, Order_Date, datepart(year, Order_Date) as year_of_order_date
from superstore_orders
where datepart(year, Order_Date) = 2020

select Order_ID, Order_Date, datepart(year, Order_Date) as year_of_order_date,
datepart(month, Order_Date) as month_of_order_date,
datepart(week, Order_Date) as week_of_order_date,
DATENAME(month, Order_Date) as month_name,
DATENAME(weekday, Order_Date) as week_name
from superstore_orders

-- add subtract from date
select Order_ID, Order_Date, DATEADD(day, 5, Order_Date) as order_date_5,
DATEADD(week, 5, Order_Date) as order_date_5,
DATEADD(day, -5, Order_Date) as order_date_5_minus
from superstore_orders

-- datediff
select Order_ID, Order_Date, Ship_Date,
datediff(day, Order_Date, Ship_Date) as date_diff_days,
datediff(week, Order_Date, Ship_Date) as date_diff_weeks
from superstore_orders

-- Case, similar to if,else, want to creates buckets
-- case statemnts always executed from top to bottom, first satisy thna stop, else check for next till satisfy
select Order_ID, Profit,
case
 when Profit < 100 then 'Low Profit'
 when Profit < 250 then 'Medium Profit'
 when Profit < 400 then 'High Profit'
 else 'very hight profit'
end as profit_category
from superstore_orders



----------------- Assignments -----------
-- Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.

-- Run the following command to add and update dob column in employee table
alter table  employee add dob date;
update employee set dob = dateadd(year,-1*emp_age,getdate())

-- 1- write a query to print emp name , their manager name and diffrence in their age (in days) 
for employees whose year of birth is before their managers year of birth

select e1.emp_name,e2.emp_name as manager_name , DATEDIFF(day,e1.dob,e2.dob) as diff_in_age
from employee e1
inner join employee e2 on e1.manager_id=e2.emp_id
where DATEPART(year,e1.dob)< DATEPART(year,e2.dob);

-- 2- write a query to find subcategories who never had any return orders in the month of november (irrespective of years)
select sub_category
from orders o
left join returns r on o.order_id=r.order_id
where DATEPART(month,order_date)=11
group by sub_category
having count(r.order_id)=0;

-- 3- orders table can have multiple rows for a particular order_id when customers buys more than 1 product in an order.
-- write a query to find order ids where there is only 1 product bought by the customer.
select order_id
from orders 
group by order_id
having count(1)=1


-- 4- write a query to print manager names along with the comma separated list(order by emp salary) of all employees directly reporting to him.
select e2.emp_name as manager_name , string_agg(e1.emp_name,',') as emp_list
from employee e1
inner join employee e2 on e1.manager_id=e2.emp_id
group by e2.emp_name


-- 5- write a query to get number of business days between order_date and ship_date (exclude weekends). 
-- Assume that all order date and ship date are on weekdays only

select order_id,order_date,ship_date ,datediff(day,order_date,ship_date)-2*datediff(week,order_date,ship_date) as no_of_business_days
from 
orders

-- 6- write a query to print 3 columns : category, total_sales and (total sales of returned orders)
select o.category,sum(o.sales) as total_sales
,sum(case when r.order_id is not null then sales end) as return_orders_sales
from orders o
-- total sales also required so doing left join
left join returns r on o.order_id=r.order_id
group by category

-- 7- write a query to print below 3 columns
-- category, total_sales_2019(sales in year 2019), total_sales_2020(sales in year 2020)
-- pivoting the data - 3 colums required
-- pivoting data in rows and converted to columns
select category,sum(case when datepart(year,order_date)=2019 then sales else 0 end) as total_sales_2019
,sum(case when datepart(year,order_date)=2020 then sales else 0 end) as total_sales_2020
from orders 
where datepart(year,order_date) in (2019, 2020)
group by category

-- 8- write a query print top 5 cities in west region by average no of days between order date and ship date.
select top 5 city, avg(datediff(day,order_date,ship_date) ) as avg_days
from orders
where region='West'
group by city
order by avg_days desc

-- 9- write a query to print emp name, manager name and senior manager name (senior manager is manager's manager)

select e1.emp_name,e2.emp_name as manager_name,e3.emp_name as senior_manager_name
from employee e1
inner join employee e2 on e1.manager_id=e2.emp_id
inner join employee e3 on e2.manager_id=e3.emp_id
