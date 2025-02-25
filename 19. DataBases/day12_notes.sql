-- lec 1o
-- window analyticial functions
-- Window Analytical functions - RANK, ROW_NUMBER, LEAD, LAG etc
------ lec - 10
---- using windows function query can be easy and very performant 
---- very important concepts to solve question
select * from employee

-- Employee with Highest salary in the departments
select * from employee
order by dept_id, salary desc;

-- Top 2 employee in each dept having highest salary
-- top 2 products in each category be sells
--- overall table you can do top2, not possible to do on department wise
-- so need to create partion on window functions
-- group by dept_id you have to take aggregation function on it

select dept_id, max(salary) from employee
group by dept_id;

-- cannot possible to find second salary, we can only do max or min 
-- top 2, top3 not possible so window function comes in account and do some ranking lot of other things

-- How it work
-- row_number is a runing number
-- over you can define window - which window you want to work
-- full table is one window
-- rn is a runing number generated based on salary 
-- Generating row_number over full table, generate number on the basis of salary in desc order
select *,
row_number() over(order by salary desc) as rn 
from employee

--- partion by dept_id, create window based on dept_id, create window for each dept_id, similar to group by but not doing any aggregation
-- function_name over(window is optional, order by)
-- window is optional given it will consider that to window, if not whole table is a window, order by is mandatory, row number is done according to that
select *,
row_number() over(partition by dept_id order by salary desc) as rn 
from employee;

-- dept_id 100 -  rn is from 1,2,3,4 -- window
-- dept_id 300 - rn is 1, 2 -- window
-- dept_id 500 - rn is 1 -- window

--- Each dept id highest slaried Employee 
-- row number is generated in select so can't used in where clause
select *,
row_number() over(partition by dept_id order by salary desc) as rn 
from employee
--where rn <= 2; -- this is syntax error not possible as rown number generated in select

-- use subquery 

select * from (
select *,
row_number() over(partition by dept_id order by salary desc) as rn 
from employee ) as A
where rn <=2

-- other way we can convert it into ctes 
with cte as (
    select *,
    row_number() over(partition by dept_id order by salary desc) as rn 
    from employee
)
select * from cte
where rn <= 2;

--- other functions
-- row_number 
--- rank() - two people with same salary get the same rank, 2, 2, skip 3 and make 4
--- give same rank to two people having same slary, next number is how many before it count 
select *,
row_number() over(order by salary desc) as rn,
rank() over(order by salary desc) as rnk 
from employee

-- in partion by can give multiple colums similar to group by 

select *,
row_number() over(partition by dept_id order by salary desc) as rn,
rank() over(partition by dept_id order by salary desc) as rnk 
from employee

-- in partion by can give multiple colums similar to group by 
-- dept_id, salary combination is one window
select *,
row_number() over(partition by dept_id order by salary desc) as rn,
rank() over(partition by dept_id, salary order by salary desc) as rnk 
from employee

-- first partition by happens within that window order_by happens
-- dense_rank is similar to rank but doesnot skip anything that is next number, same order than skip to next number by rank
select *,
row_number() over(partition by dept_id order by salary desc) as rn,
rank() over(partition by dept_id order by salary desc) as rnk,
dense_rank() over(partition by dept_id order by salary desc) as d_rnk
from employee

-- rank same slary are getting same rank
-- top 2 employee in each dept -- get rank and <=2
-- if slary same pick employee having lesser age so do order by in age in over
-- difference in rank, dense_rank, row_number for the data in interview -- they will ask

-- query to print top 5 selleing products from each category by sales
select * from superstore_orders

-- category, product_id, total_sales -- first get this
--- this is wroung
-- select * from (
-- select *,
-- row_number() over(partition by Category order by Sales desc) as rn 
-- from superstore_orders ) as A
-- where rn <=5
---

-- category, product_id, total_sales -- first get this, now apply row number 
-- before applying window function think what granularity you are applying on it
-- numeros interview question in Internet, top 5 top salary 
with cat_prod_sales as
(
    select Category, Product_ID, sum(Sales) as category_sales
    from superstore_orders
    group by Category, Product_ID 
),
rank_sales as (select *,
rank() over(partition by Category order by category_sales desc) as rn
from cat_prod_sales)
select * 
from rank_sales
where rn <= 5;

-- other way to write
-- first group by happening than rank function run on top of it
with 
rank_sales as (select Category, Product_ID,
rank() over(partition by Category order by sum(Sales) desc) as rn
from superstore_orders
group by Category, Product_ID 
)
select * 
from rank_sales
where rn <= 5;


-- lead, pass two mandaotry params
-- lead talk with prev rows and next one also
-- do order by salary and look to next row lead(emp_id, 1), 1 means next row
-- lead(emp_id, 2), skip two next rows, look 2nd row from first row
-- lead(emp_id, 1, 999) if next row is not there than 999 is default, you can pass col also
-- no value after lead if at last row put default specified  

select *,
lead(emp_id, 1) over(order by salary desc) as lead_emp,
row_number() over(order by salary desc) as rn,
rank() over(order by salary desc) as rnk 
from employee;


select *,
lead(emp_id, 1) over(partition by dept_id order by salary desc) as lead_emp
from employee;

-- lag means prev, backward, lead means next, forward
-- same thing is achieved by using lead salary asc
select *,
lead(emp_id, 1) over(partition by dept_id order by salary desc) as lead_emp,
lag(emp_id, 1) over(partition by dept_id order by salary desc) as leg_emp
from employee;

-- year wise sales, you will see yar wise growth by using lead or lag, and calculate diff, when same row do any calculation

--- Assigments -----
-- Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.


-- 1- write a query to print 3rd highest salaried employee details for each department (give preferece to younger employee in case of a tie). 
-- In case a department has less than 3 employees then print the details of highest salaried employee in that department.


with rnk as (
select *, dense_rank() over(partition by dept_id order by salary desc) as rn
from employee)
,cnt as (select dept_id,count(1) as no_of_emp from employee group by dept_id)
select
rnk.*
from 
rnk 
inner join cnt on rnk.dept_id=cnt.dept_id
where rn=3 or  (no_of_emp<3 and rn=1) 

--this solution is usning a concept covered in next class 

with rnk as (
select *, dense_rank() over(partition by dept_id order by salary desc) as rn
,count(1) over(partition by dept_id ) as no_of_emp
from employee)
select
*
from 
rnk 
where rn=3 or  (no_of_emp<3 and rn=1) 


-- 2- write a query to find top 3 and bottom 3 products by sales in each region.

with region_sales as (
select region,product_id,sum(sales) as sales
from orders
group by region,product_id
)
,rnk as (select *, rank() over(partition by region order by sales desc) as drn
, rank() over(partition by region order by sales asc) as arn
from region_sales
)
select region,product_id,sales,case when drn <=3 then 'Top 3' else 'Bottom 3' end as top_bottom
from rnk
where drn <=3 or arn<=3


-- 3- Among all the sub categories..which sub category had highest month over month growth by sales in Jan 2020.

with sbc_sales as (
select sub_category,format(order_date,'yyyyMM') as year_month, sum(sales) as sales
from orders
group by sub_category,format(order_date,'yyyyMM')
)
, prev_month_sales as (select *,lag(sales) over(partition by sub_category order by year_month) as prev_sales
from sbc_sales)
select  top 1 * , (sales-prev_sales)/prev_sales as mom_growth
from prev_month_sales
where year_month='202001'
order by mom_growth desc


-- 4- write a query to print top 3 products in each category by year over year sales growth in year 2020.

with cat_sales as (
select category,product_id,datepart(year,order_date) as order_year, sum(sales) as sales
from orders
group by category,product_id,datepart(year,order_date)
)
, prev_year_sales as (select *,lag(sales) over(partition by category,product_id order by order_year) as prev_year_sales
from cat_sales)
,rnk as (
select   * ,rank() over(partition by category order by (sales-prev_year_sales)/prev_year_sales desc) as rn
from prev_year_sales
where order_year='2020'
)
select * from rnk where rn<=3



-- 5- create below 2 tables 

create table call_start_logs
(
phone_number varchar(10),
start_time datetime
);
insert into call_start_logs values
('PN1','2022-01-01 10:20:00'),('PN1','2022-01-01 16:25:00'),('PN2','2022-01-01 12:30:00')
,('PN3','2022-01-02 10:00:00'),('PN3','2022-01-02 12:30:00'),('PN3','2022-01-03 09:20:00')
create table call_end_logs
(
phone_number varchar(10),
end_time datetime
);
insert into call_end_logs values
('PN1','2022-01-01 10:45:00'),('PN1','2022-01-01 17:05:00'),('PN2','2022-01-01 12:55:00')
,('PN3','2022-01-02 10:20:00'),('PN3','2022-01-02 12:50:00'),('PN3','2022-01-03 09:40:00')
;

-- write a query to get start time and end time of each call from above 2 tables.Also create a column of call duration in minutes.  Please do take into account that
-- there will be multiple calls from one phone number and each entry in start table has a corresponding entry in end table.

-- dpo join om phoen number and rank
select *,row_number() over(partition by phone_number order by start_time) as rn  from call_start_logs
inner join (select *,row_number() over(partition by phone_number order by end_time) as rn  from call_end_logs) e
on s.phone_number = e.phone_number and s.rn=e.rn;


select s.phone_number,s.rn,s.start_time,e.end_time, datediff(minute,start_time,end_time) as duration
from 
(select *,row_number() over(partition by phone_number order by start_time) as rn  from call_start_logs) s
inner join (select *,row_number() over(partition by phone_number order by end_time) as rn  from call_end_logs) e
on s.phone_number = e.phone_number and s.rn=e.rn;



