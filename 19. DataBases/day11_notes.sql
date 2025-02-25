-- LEC 9, subQueris and CTES
--- SUB QUERIS
select * from superstore_orders

-- why need subquery
-- how to find average order value ? 
select avg(Sales) from superstore_orders
-- there is a problems in this, just sum/number of row its wrong
-- avg order value is wroungh, order have more than one products which means required some intermediate result to reach
-- first drive based on order_id and take average 
-- first find what is sales based on order_id than take average, need of intermediate result to hold and so on top of it.
-- where subquery comes in pictures


-- intermediate result, virtual table consider its as table orders_aggregated
select Order_ID, Sum(Sales) as order_sales
from superstore_orders
group by Order_ID

-- find avrgae order value
select avg(order_sales) from
(select Order_ID, Sum(Sales) as order_sales
from superstore_orders
group by Order_ID) as orders_aggregated
-- 458

-- find all order whose slaes is greater than average order value
-- use of sub query in from clause

select Order_ID
from superstore_orders
group by Order_ID
having sum(Sales) > 
(select avg(order_sales) as average_order_value from
(select Order_ID, Sum(Sales) as order_sales
from superstore_orders
group by Order_ID) as orders_aggregated)


select * from employee;
select * from dept;

-- Emplyee departmnet is not present in department table -- solve using join 
-- lets solve using sub query, use in where clause 

select * from employee
where dept_id not in (
    -- put sub query here
    select dep_id from dept
)

-- not get full result you will get only dep_id
select dept_id from employee
except
select dep_id from dept

-- when using filter condition pass one field in subquery select except Exist

-- use of sub quey in select clause
select *, (select avg(salary) from employee) from employee
-- calculating avg slary and putting to all the rows

select *, (select avg(salary) from employee as avg_salary) from employee
where dept_id not in (
    -- put sub query here
    select dep_id from dept
)

-- select avg(salary) from employee excuted first, than on main query putting the filter
-- Another way of doing is 
select A.*, B.*
from 
(select Order_ID, sum(Sales) as order_sales
from superstore_orders
group by Order_ID) as A  -- table A
-- join these two data sets
inner join 
-- this query always give one value
(select avg(order_sales) as average_order_value from
(select Order_ID, Sum(Sales) as order_sales
from superstore_orders
group by Order_ID) as orders_aggregated) as B -- table B
on 1=1
where order_sales > average_order_value;

-- subquery of table A, subquery of table B and join them 

-- 1=1 no common fields so want to join so given always true
-- join on table
-- select
--    from table A
--    inner join table b on col=col

-- IMP Concepts
-- Along with EMPY_ID i want to see avag slary in there departments
-- departmnet wise average salary 
-- dep_id, avag_salary -- intermediate result 
-- there is employee table 
-- join this two tables on dep_id and get the result


select * from employee  -- table 1
select dept_id, avg(salary) as avg_dep_salary -- table 2
from employee
group by dept_id

-- Now join table_1, and table 2 on dept_id

select e.*, d.avg_dep_salary from employee as e
inner join 
(select dept_id, avg(salary) as avg_dep_salary
from employee
group by dept_id) as d
on e.dept_id = d.dept_id

-- when you have confusion write just what you want, write inner query and use it

-- Question to solve 
create table icc_world_cup
(
Team_1 Varchar(20),
Team_2 Varchar(20),
Winner Varchar(20)
);
INSERT INTO icc_world_cup values('India','SL','India');
INSERT INTO icc_world_cup values('SL','Aus','Aus');
INSERT INTO icc_world_cup values('SA','Eng','Eng');
INSERT INTO icc_world_cup values('Eng','NZ','NZ');
INSERT INTO icc_world_cup values('Aus','India','India');


-- 1- write a query to produce below output from icc_world_cup table.
-- team_name, no_of_matches_played , no_of_wins , no_of_losses
-- India, 2, 2, 0

select * from icc_world_cup

-- power of subquery
-- need all teams two diffent colums team_1. team_2
select Team_1 as team_name, case when Team_1= Winner then 1 else 0 end as win_flag
from icc_world_cup
union ALL
select Team_2 as team_name, case when Team_2= Winner then 1 else 0 end as win_flag
from icc_world_cup

-- from above table we can find no_of_matches_played , no_of_wins , no_of_losses
-- wrap in sub query
-- hold the result in inner query and use it
-- count(1) -- total number of matched played, you can use count(*), count number of rows

select team_name, count(1) as no_of_matches_played, sum(win_flag) as no_of_wins, count(1) - sum(win_flag) as no_of_losses
from
(select Team_1 as team_name, case when Team_1= Winner then 1 else 0 end as win_flag
from icc_world_cup
union ALL
select Team_2 as team_name, case when Team_2= Winner then 1 else 0 end as win_flag
from icc_world_cup) as A
group by team_name;

--
--- CTES
-- common table expressions
-- solve same question using ctes,  subquery and ctes are very similar
-- with A as (Query here ), A is the table with result of inner query



with A as (
    select Team_1 as team_name, case when Team_1= Winner then 1 else 0 end as win_flag
    from icc_world_cup
    union ALL
    select Team_2 as team_name, case when Team_2= Winner then 1 else 0 end as win_flag
    from icc_world_cup
)
select team_name, count(1) as no_of_matches_played, sum(win_flag) as no_of_wins, count(1) - sum(win_flag) as no_of_losses
from A
group by team_name;



with dep as (
    select dept_id, avg(salary) as avg_dep_salary
    from employee
    group by dept_id
)
select e.*, d.avg_dep_salary from employee as e
inner join dep as d
on e.dept_id = d.dept_id;

-- CTES query are more stuctured 
-- nested query0 ( query1 ( query2) )
-- ctes query1
-- query 2
-- query 0 
-- redability is good in CTES, use always CTES


-- doing 2 times same query order wise order sales 

select A.*, B.*
from 
(select Order_ID, sum(Sales) as order_sales
from superstore_orders
group by Order_ID) as A  -- table A
-- join these two data sets
inner join 
-- this query always give one value
(select avg(order_sales) as average_order_value from
(select Order_ID, Sum(Sales) as order_sales
from superstore_orders
group by Order_ID) as orders_aggregated) as B -- table B
on 1=1
where order_sales > average_order_value;

-- convert in ctes
-- this can be used in order_wise_sales multiple times, performnace is better
-- easy to database to hold at one time and use at multiple places
with order_wise_sales as (
    select Order_ID, sum(Sales) as order_sales
    from superstore_orders
    group by Order_ID
), B as (select avg(order_sales) as average_order_value from
order_wise_sales as orders_aggregated)
select order_wise_sales.*, B.*
from order_wise_sales
inner join 
B
on 1=1
where order_sales > average_order_value;

---- simple subquery no need to create ctes 

select *, (select avg(salary) from employee as avg_salary) from employee
where dept_id not in (
    -- put sub query here
    select dep_id from dept
)
-- no making much sense on CETS
with depts as (
    select dep_id from dept
)
select * from employee
where dept_id in (select dep_id from depts)


------ problems ------

-- Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.

-- 1- write a query to find premium customers from orders data. Premium customers are those who have done more orders than average no of orders per customer.

with no_of_orders_each_customer as (
select customer_id,count(distinct order_id) as no_of_orders
from orders 
group by customer_id)
select * from 
no_of_orders_each_customer where no_of_orders > (select avg(no_of_orders) from no_of_orders_each_customer)

-- 2- write a query to find employees whose salary is more than average salary of employees in their department


select e.* from employee e
inner join (select dept_id,avg(salary) as avg_sal from employee group by dept_id)  d
on e.dept_id=d.dept_id
where salary>avg_sal

-- 3- write a query to find employees whose age is more than average age of all the employees.


select * from employee 
where emp_age > (select avg(emp_age) from employee)


-- 4- write a query to print emp name, salary and dep id of highest salaried employee in each department 


select e.* from employee e
inner join (select dept_id,max(salary) as max_sal from employee group by dept_id)  d
on e.dept_id=d.dept_id
where salary=max_sal

-- 5- write a query to print emp name, salary and dep id of highest salaried employee overall


select * from employee 
where salary = (select max(salary) from employee)


-- 6- write a query to print product id and total sales of highest selling products (by no of units sold) in each category

with product_quantity as (
select category,product_id,sum(quantity) as total_quantity
from orders 
group by category,product_id)
,cat_max_quantity as (
select category,max(total_quantity) as max_quantity from product_quantity 
group by category
)
select *
from product_quantity pq
inner join cat_max_quantity cmq on pq.category=cmq.category
where pq.total_quantity  = cmq.max_quantity