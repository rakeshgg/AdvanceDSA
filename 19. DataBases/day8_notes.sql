-- 7. set operation

--- String Functions
-- len() -- count spaces also not counting traling spaces
-- left(Customer_Name, 4), left character from left
--- SUBSTRING(Customer_Name, 4, 5) start from 4 and take 5 char
--- CHARINDEX(char, colum, positio_to_start) -- position of first occurance char in columns give index, positio_to_start default to 0
--- CONCAT(Order_ID, '', Customer_Name,)
--- REPLACE(Order_ID, 'CA', 'PB'), replace ca with pb, look for full string continous 
--- TRANSLATE(Customer_Name, 'AG', 'TP'), translate A -> T, G --> P, one to one mapping, translate one by one
--- REVERSE(Customer_Name), reverse the string
--- TRIM -- removed leading and tralling white spaces from string

select Order_ID, Customer_Name
,len(Customer_Name) as len_count
,left(Customer_Name, 4) as name_4
,right(Customer_Name, 4) as name_r
,SUBSTRING(Customer_Name, 4, 5) as substr_4_5
,SUBSTRING(Order_ID, 4, 4) as order_year
,CHARINDEX(' ', Customer_Name) as space_position
,CONCAT(Order_ID, '-', Customer_Name)
,Order_ID + ' ' + Customer_Name
,left(Customer_Name, CHARINDEX(' ', Customer_Name)) as first_name
,REPLACE(Order_ID, 'CA', 'PB') as replace_cb
,TRANSLATE(Customer_Name, 'AG', 'TP') as transalte_ag
,REVERSE(Customer_Name) as reverse_name
,TRIM(' rk  ') as trim
from superstore_orders; 


--- Null handling functions
--- isnull(city, 'unknown') relpace city value NULL to unknown, if value that value comes
--- COALESCE(City,State, Region, 'unknown') same as isnull but can pass more columns if city null check for state, if state null check for region,
--- COALESCE, always use

select Order_ID, City, isnull(city, 'unknown') as new_city
,COALESCE(City,State, Region, 'unknown') as newW_city
,CAST(Sales)
from superstore_orders
order by City

--- Numeric function
---- CAST(Sales as int) convert data type
--- ROUND(Sales, 1) round upto 1 digits

select top 5 Order_ID, Sales
,CAST(Sales as int) as sales_int
,ROUND(Sales, 1) as sales_round
from superstore_orders


----- SET QUERIES ----------
--- one table, multiple tables
--- differnt table having different region data want to combine the data, generate data by combing multiple table
--- set -- union table combine -- Horizonatal combination
-- join - vertical combination of 


--union all, union
create table orders_west
(
order_id int,
region varchar(10),
sales int
);


create table orders_east
(
order_id int,
region varchar(10),
sales int
);

insert into orders_west values(1,'west',100),(2,'west',200);
insert into orders_east values(3,'east',100),(4,'east',300);
insert into orders_west values(3,'east',100)
insert into orders_west values(1,'west',100)

select * from orders_west
select * from orders_east

-- same number of columns and data type is compatible for set operations
-- union all, gives total number of rows, just combine data, duplicate also there
-- union -- remove duplicates, rows
select * from orders_west
union all
select * from orders_east;

select * from orders_west
union
select * from orders_east;


select * from orders_west
intersect
select * from orders_east;

select order_id, sales from orders_west
intersect
select order_id, sales from orders_east;

-- orders_west - orders_west
-- only union all give duplicates, other all remove duplicates
select order_id, sales from orders_west
except 
select order_id, sales from orders_east;


(select * from orders_west
except 
select * from orders_east)
union all
(select * from orders_east
except 
select * from orders_west)

-- handy on testing -- which rows are differnt and data is not correct