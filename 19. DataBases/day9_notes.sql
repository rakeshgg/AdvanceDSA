-- LEC - 8, SQL Interview questions

-- Please solve these problems. You have option to solve them in MySQL, sql server and postgres. All are free questions.

-- 1- https://www.namastesql.com/coding-problem/38-product-reviews
-- 2- https://www.namastesql.com/coding-problem/61-category-sales-part-1
-- 3- https://www.namastesql.com/coding-problem/62-category-sales-part-2
-- 4- https://www.namastesql.com/coding-problem/71-department-average-salary
-- 5- https://www.namastesql.com/coding-problem/72-product-sales
-- 6- https://www.namastesql.com/coding-problem/73-category-product-count
-- 7- https://www.namastesql.com/coding-problem/103-employee-mentor


-- Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.
-- Run below table script to create icc_world_cup table:

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

-- tem_name can be from Team_1, Team_2 colums - in this case use set operations
-- how to decide winner team_name and winner is same than make some flags

with all_teams as 
(select team_1 as team, case when team_1=winner then 1 else 0 end as win_flag from icc_world_cup
union all
select team_2 as team, case when team_2=winner then 1 else 0 end as win_flag from icc_world_cup)
select team,count(1) as total_matches_played , sum(win_flag) as matches_won,count(1)-sum(win_flag) as matches_lost
from all_teams
group by team

-- 2- write a query to print first name and last name of a customer using orders table(everything after first space can be considered as last name)
-- customer_name, first_name,last_name

select customer_name , trim(SUBSTRING(customer_name,1,CHARINDEX(' ',customer_name))) as first_name
, SUBSTRING(customer_name,CHARINDEX(' ',customer_name)+1,len(customer_name)-CHARINDEX(' ',customer_name)+1) as second_name
from orders



-- Run below script to create drivers table:

create table drivers(id varchar(10), start_time time, end_time time, start_loc varchar(10), end_loc varchar(10));
insert into drivers values('dri_1', '09:00', '09:30', 'a','b'),('dri_1', '09:30', '10:30', 'b','c'),('dri_1','11:00','11:30', 'd','e');
insert into drivers values('dri_1', '12:00', '12:30', 'f','g'),('dri_1', '13:30', '14:30', 'c','h');
insert into drivers values('dri_2', '12:15', '12:30', 'f','g'),('dri_2', '13:30', '14:30', 'c','h');

-- 3- write a query to print below output using drivers table. Profit rides are the no of rides where end location of a ride is same as start location of immediate next ride for a driver
-- id, total_rides , profit_rides
-- dri_1,5,1
-- dri_2,2,0
-- profit rides is when end loc of rides in imediately same as start location of next ride
-- dri_1, 1 profit rides
-- if look row wise we can't get it, look to next row some how
-- join make two table self join, driver_id, end_loc, start loc of table1, table2 equals
-- and end_tme and start time is same

-- profit rides, case of self join
-- count never count null
select d1.id as driver_id, count(1) as total_rides, count(d2.id) as profit_rides
from drivers d1
left join drivers d2 on d1.id=d2.id, d1.end_loc=d2.start_loc
         and d1.end_time=d2.start_time
group by d1.id


--lead function window
select id, count(1) as total_rides
,sum(case when end_loc=next_start_location then 1 else 0 end ) as profit_rides
from (
select *
, lead(start_loc,1) over(partition by id order by start_time asc) as next_start_location
from drivers) A
group by id;

--self join
with rides as (
select *,row_number() over(partition by id order by start_time asc) as rn
from drivers)
select r1.id , count(1) total_rides, count(r2.id) as profit_rides
from rides r1
left join rides r2
on r1.id=r2.id and r1.end_loc=r2.start_loc and r1.rn+1=r2.rn
group by r1.id


-- 4- write a query to print customer name and no of occurence of character 'n' in the customer name.
-- customer_name , count_of_occurence_of_n
select customer_name , len(customer_name)-len(replace(lower(customer_name),'n','')) as count_of_occurence_of_n
from orders


-- 5-write a query to print below output from orders data. example output
-- hierarchy type,hierarchy name ,total_sales_in_west_region,total_sales_in_east_region
-- category , Technology, ,
-- category, Furniture, ,
-- category, Office Supplies, ,
-- sub_category, Art , ,
-- sub_category, Furnishings, ,
--and so on all the category ,subcategory and ship_mode hierarchies 
-- 3 type of hiearchy

-- 'category' as hierarchy_type this is literal values add all in colums
-- union - remove duplicate - extra work
-- if no duplicate always use union all, so it will not do extra work of removing -- --duplicate as union does optimized queries
-- colum name is always taken from first query, hierarchy_type, hierarchy_name, total_sales_in_west_region, total_sales_in_east_region
-- you can remove in other query still work
select 
'category' as hierarchy_type,category as hierarchy_name
,sum(case when region='West' then sales end) as total_sales_in_west_region
,sum(case when region='East' then sales end) as total_sales_in_east_region
from orders
group by category
union all
select 
'sub_category',sub_category
,sum(case when region='West' then sales end) as total_sales_in_west_region
,sum(case when region='East' then sales end) as total_sales_in_east_region
from orders
group by sub_category
union all
select 
'ship_mode ',ship_mode 
,sum(case when region='West' then sales end) as total_sales_in_west_region
,sum(case when region='East' then sales end) as total_sales_in_east_region
from orders
group by ship_mode


-- 6- the first 2 characters of order_id represents the country of order placed . write a query to print total no of orders placed in each country
-- (an order can have 2 rows in the data when more than 1 item was purchased in the order but it should be considered as 1 order)

select left(order_id,2) as country, count(distinct order_id) as total_orders
from orders 
group by left(order_id,2)
