/*
 In computer drive dbo is bydefult schema
 drive have multiple folder 
 schema is a Folder, dbo schema is defualt where multiple table by defult can be
 created if schema not provided.
 schema is different folder within database

*/
--DDL - > data definition language
create table amazon_orders
(
order_id integer,
order_date date,
product_name varchar(100),
total_price decimal(6,2),
payment_method varchar(20)
);
--delete a table -- This is DDL, changing the defination of language
--drop table amazon_orders;

--DML -> data Manipulation language - manupulating data, insert, update
insert into amazon_orders values(1,'2022-10-01','Baby Milk',30.5,'UPI');
insert into amazon_orders values(2,'2022-10-02','Baby Powder',130,'Credit Card');

insert into amazon_orders values(3,'2022-10-01','Baby cream',30.5,'UPI');
insert into amazon_orders values(4,'2022-10-02','Baby soap',130,'Credit Card');

--to delete data, delete all data from table, DML
delete from amazon_orders;


-- DQL -> data querying language, not changing anything in data
select * from amazon_orders;
--limiting columns or selecting specific columns
select product_name,order_date,total_price from amazon_orders;
--limiting rows some db have Limit, offset
select top 1 * from amazon_orders;
-- last 5 will come with order_by
--data sorting
select * from amazon_orders
order by order_date desc,product_name desc,payment_method;

/*
data types--
integer -> 1,2,3,-1,-2
date - > '2020-11-01'
varchar(100) - > 'baby milk'
decimal(5,2) -> 1234.45

drive--folder1
drive --folder2

*/
-- how to craete schema hr is a schema
create table hr.test (
)
