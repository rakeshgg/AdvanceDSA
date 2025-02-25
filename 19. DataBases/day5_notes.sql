-- NULL Filter 

select Order_ID from superstore_orders;

update superstore_orders
set City = NULL
where Order_ID in ('CA-2020-161389', 'US-2021-156909');

select * from superstore_orders
where Order_ID in ('CA-2020-161389', 'US-2021-156909');

select * from superstore_orders
where City is NULL

select * from superstore_orders
where City is not NULL;

--- aggregation: generate some report
-- count number of record in tables
-- take all rows and do aggregation
select count(*) as cnt,
sum(Sales) as total_sales,
max(Sales) as max_sales,
min(Profit) as min_profit,
avg(Profit) as avg_profit
from superstore_orders;

-- get all of above at region level where gropp by keyword comes
-- it is similar to pivot table in excel
select region, count(*) as cnt,
sum(Sales) as total_sales,
max(Sales) as max_sales,
min(Profit) as min_profit,
avg(Profit) as avg_profit
from superstore_orders
group by Region;

-- similar to we use distict function
-- grop all value in that columns together
-- advatage is you have aggregated value as well
select region
from superstore_orders
group by Region;

select distinct region
from superstore_orders;

-- combination of two columns
select Region, Category, sum(Sales) as total_sales
from superstore_orders
group by Region, Category;

-- Column 'superstore_orders.Category' is invalid in the select list because it is not contained in either an aggregate function or the GROUP BY clause.
-- combing multiple rows of Region into one but saying give category which is not possible
-- **if using group by than in select clause columns only are possible which present in group by or aggregated columns
select Region, Category, sum(Sales) as total_sales
from superstore_orders
group by Region;

-- order of Execution
-- from than where and on remaning rows grouping will happens
select Region, sum(Sales) as total_sales
from superstore_orders
where Profit > 50
group by Region;

--- from,  where, group by, select, order by, top, execution order
--- order of keyword in query is also in same same order
select top 2 Region, sum(Sales) as total_sales
from superstore_orders
where Profit > 50
group by Region
order by total_sales desc;

--- filter on grouping result
--- total_sales is aggragted function and run after where clause so not possible to do in where
-- having used with group by or after group by
-- aggregate the data and apply having filter
-- from, where, group, having, select, order by
-- what is there in group by you can use in having
-- having is meant for aggregate, group filter, aggrgation is costly
-- where is applied at colum level 
select Sub_Category, sum(Sales) as total_sales
from superstore_orders
-- where total_sales > 1000
where Profit > 50
group by Sub_Category
-- not valid columns
-- having total_sales > 1000
having sum(Sales) > 1000
order by total_sales desc;

--- Column 'superstore_orders.Order_Date' is invalid in the HAVING clause because it is not contained in either an aggregate function or the GROUP BY clause.
--- after grouping having filter is applied
select Sub_Category, sum(Sales) as total_sales
from superstore_orders
group by Sub_Category
-- having Order_Date > '2020-01-01'
having max(Order_Date) > '2020-01-01'
order by total_sales desc;

-- ROW level filter -- where
-- aggregated level filter -- having
select Sub_Category, sum(Sales) as total_sales
from superstore_orders
where Order_Date > '2020-01-01'
group by Sub_Category
order by total_sales desc;

-- count doesnot count NULL values, ignore NUll values
-- any aggrgate function also ignore Null values in rows
-- avg -- total/count
-- any aggrgate function just ignore null values
select count(distinct Category),
-- goes each rows and count 1 that number of times
count(1),
count(City),
sum(Sales)
from superstore_orders



--Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.

--1- write a update statement to update city as null for order ids :  CA-2020-161389 , US-2021-156909

update orders set city=null where order_id in ('CA-2020-161389','US-2021-156909')

--2- write a query to find orders where city is null (2 rows)
select * from orders where city is null


--3- write a query to get total profit, first order date and latest order date for each category
select category , sum(profit) as total_profit, min(order_date) as first_order_date
,max(order_date) as latest_order_date
from orders
group by category 


--4- write a query to find sub-categories where average profit is more than the half of the max profit in that sub-category
select sub_category
from orders
group by sub_category
having avg(profit) > max(profit)/2


--5- create the exams table with below script;
create table exams (student_id int, subject varchar(20), marks int);

insert into exams values (1,'Chemistry',91),(1,'Physics',91),(1,'Maths',92)
,(2,'Chemistry',80),(2,'Physics',90)
,(3,'Chemistry',80),(3,'Maths',80)
,(4,'Chemistry',71),(4,'Physics',54)
,(5,'Chemistry',79);

-- write a query to find students who have got same marks in Physics and Chemistry.

-- same marks in physics chemestry - intresetd in physics, chemestry so use where
-- group on student id, for smae student checking marks
select student_id, count(*) as total_record, count(distinct(marks)) as distinct_mark
from exams
where subject in ('Physics', 'Chemistry')
group by student_id
having count(*) = 2 and count(distinct marks) = 1;

-- another approch -- max two subjects is there
-- student id, marks have 2 records
select student_id, marks, count(1) as total_rows
from exams
where subject in ('Physics', 'Chemistry')
group by student_id, marks
having count(1)=2
order by student_id;


-- 6- write a query to find total number of products in each category.
select category,count(distinct product_id) as no_of_products
from orders
group by category


-- 7- write a query to find top 5 sub categories in west region by total quantity sold
select top 5  sub_category, sum(quantity) as total_quantity
from orders
where region='West'
group by sub_category
order by total_quantity desc


-- 8- write a query to find total sales for each region and ship mode combination for orders in year 2020
select region,ship_mode ,sum(sales) as total_sales
from orders
where order_date between '2020-01-01' and '2020-12-31'
group by region,ship_mode