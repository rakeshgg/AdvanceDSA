--- LEC -11, Aggregation with windows function

-- year wise sales, you will see yar wise growth by using lead or lag, and calculate diff, when same row do any calculation
--- Lec - 11
-- Aggregation on Window Functions
select * 
from employee;

-- avarage salary in each departments
-- subquery got dept wise avag salary and join with dept id and got the avag salary
-- we can achieve using of window functions withoout joins
-- go to each partion and do average
-- creating window of dept_id, within that windo taking the max and giving each row
-- avg, max --- no order by mandatory, lead, lag its required
select * 
,avg(salary) over(partition by dept_id) as avg_salary
,max(salary) over(partition by dept_id) as max_salary
,count(salary) over(partition by dept_id) as count_salary
from employee;

-- if order by given than it will give cumulative sum, cumulative max !.e runing max
select * 
,sum(salary) over(partition by dept_id order by emp_age asc) as dept_runing_salary
-- on defining order by as per that it will give the runing sum, cumulative sum
,sum(salary) over(partition by dept_id) as sum_salary
,max(salary) over(partition by dept_id order by salary asc) as max_runing_salary
,max(salary) over(partition by dept_id) as max_salary
from employee;

-- if there are duplicate just consider as as one
-- runing some based on order by, you can also supply partition by
-- order by make it runing sum
select * 
,sum(salary) over(order by salary, dept_id desc) as runing_salary
from employee;

-- rolling slaes, 3 month sales
-- sum of prev two salary as current row, sum prev two + current row -- this is rolling sum

select * 
,sum(salary) over(order by emp_id rows between 2 preceding and current row) as rolling_3_salary
from employee;


--- following is next, preceding is previous , next + curr row + prev
select * 
,sum(salary) over(order by emp_id rows between 1 preceding and 1 following) as rolling_3_salary
from employee;

select * 
,sum(salary) over(partition by dept_id order by emp_id rows between 2 preceding and 2 following) as rolling_5_salary
from employee;

-- unbounded -- all the row to previous,, all the previous rows to currnet 
-- work as all the prev row and current row -- prev row to current row
select * 
,sum(salary) over(order by emp_id rows between unbounded preceding and current row) as rolling_5_salary
from employee;

select * 
,sum(salary) over(order by emp_id rows between unbounded preceding and unbounded following) as rolling_all_salary
from employee;

select * 
,first_value(salary) over(order by salary) as first_salary
,first_value(salary) over(order by salary desc) as last_salary_using_first
,last_value(salary) over(order by salary rows between unbounded preceding and unbounded following) as last_salary
from employee;


select order_id,sales,sum(sales) over( order by order_id,row_id) as running_sales
from orders;

with month_wise_sales as 
(select datepart(year,order_date) as year_order,datepart(month,order_date) as month_order,sum(sales) as total_sales
from orders
group by datepart(year,order_date),datepart(month,order_date))
select 
year_order,month_order,total_sales
,sum(total_sales) over(order by year_order,month_order rows between 2 preceding and current row) as rolling_3_sales
from month_wise_sales;

--update,delete advance
--exist and not exists
--pivot and unpivot
--stored procedure
--indexes --performance

-- 1- write a sql to find top 3 products in each category by highest rolling 3 months total sales for Jan 2020.


with xxx as (select category,product_id,datepart(year,order_date) as yo,datepart(month,order_date) as mo, sum(sales) as sales
from orders 
group by category,product_id,datepart(year,order_date),datepart(month,order_date))
,yyyy as (
select *,sum(sales) over(partition by category,product_id order by yo,mo rows between 2 preceding and current row ) as roll3_sales
from xxx)
select * from (
select *,rank() over(partition by category order by roll3_sales desc) as rn from yyyy 
where yo=2020 and mo=1) A
where rn<=3

-- 2- write a query to find products for which month over month sales has never declined.


with xxx as (select product_id,datepart(year,order_date) as yo,datepart(month,order_date) as mo, sum(sales) as sales
from orders 
group by product_id,datepart(year,order_date),datepart(month,order_date))
,yyyy as (
select *,lag(sales,1,0) over(partition by product_id order by yo,mo) as prev_sales
from xxx)
select distinct product_id from yyyy where product_id not in
(select product_id from yyyy where sales<prev_sales group by product_id)

-- 3- write a query to find month wise sales for each category for months where sales is more than the combined sales of previous 2 months for that category.

with xxx as (select category,datepart(year,order_date) as yo,datepart(month,order_date) as mo, sum(sales) as sales
from orders 
group by category,datepart(year,order_date),datepart(month,order_date))
,yyyy as (
select *,sum(sales) over(partition by category order by yo,mo rows between 2 preceding and 1 preceding ) as prev2_sales
from xxx)
select * from yyyy where  sales>prev2_sales