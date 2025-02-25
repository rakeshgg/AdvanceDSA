
-- creating table 
create table amazon_orders
(
order_id integer,
order_date date,
product_name varchar(100),
total_price decimal(6,2),
payment_method varchar(20)
);

select * from amazon_orders;
insert into amazon_orders values(3,'2022-10-01','Baby cream',30.5,'UPI');
insert into amazon_orders values(4,'2022-10-02','Baby soap',130,'Credit Card');
select * from amazon_orders;

-- order_date is a date field created during creation of table, latter i want to store time also
-- what time more traffic do anlaytics
/* How to change the field type, as table is already created using ALTER commands 
   if want to change the data type than 
   drop table than will create with new data type but problem is loose all the data
   so alter table come in pic which help to alter the field type
*/

-- chnage data type of columns
alter table amazon_orders alter column order_date datetime; -- DDL
select * from amazon_orders;

insert into amazon_orders values(4,'2022-10-02 12:05:12','Baby soap',130,'Credit Card');
-- alter table command is DDL or DML, its DDL as changing the defination of language, table stucture changed
-- want to add more columns if required, if new col added than add at last

alter table amazon_orders add username varchar(20);
-- username is added no value having NULL, NULL means Unknown, dont know the value store NULL
insert into amazon_orders values(4,'2022-10-02 12:05:12',null,130,'Credit Card', 'rk');
-- in backend if alter than backend programe need to be updated

--  add column in exiting table
alter table amazon_orders add category varchar(20);
-- want to delte this columns as not required 
-- delete column in exiting table
alter table amazon_orders drop column category;

/* 
you cannot alter anydata type to any data type 
data type should be compatible, if no record in table than you can change to any type
int to date time not possible
if table is empty we can change from any date type to anydate type which is compatible
can chnage to higher data type
varchar can accomodate anything, varchar take more memory
YY-MM-DD is the formats
you can change the formats of date at sql server level not column level if required
*/

-- constraints, restiction on adding values at column level
create table a_amazon_orders
(
seq_no integer,
order_id integer not NULL UNIQUE, -- not null constraints, unique constarints
order_date date,
product_name varchar(100),
total_price decimal(6,2),
payment_method varchar(20) check (payment_method in ('UPI', 'CREDIT CARD')), -- check constraints
discount integer check (discount <= 20), -- check consttaints
category varchar(20) default 'Means Wear' -- if no value bu defult means wear
primary key (seq_no)
);

insert into a_amazon_orders values(null,'2022-10-02','Baby soap',130,'Credit Card');
-- Cannot insert the value NULL into column 'order_id', table 'master.dbo.a_amazon_orders'; column does not allow nulls. INSERT fails.

-- drop table a_amazon_orders;
insert into a_amazon_orders values(1,'2022-10-02','Baby soap',130,'Internet Banking');
-- The INSERT statement conflicted with the CHECK constraint "CK__a_amazon___payme__1EF99443". The conflict occurred in database "master", table "dbo.a_amazon_orders", column 'payment_method'.
insert into a_amazon_orders values(1,'2022-10-02','Baby soap',130,'UPI', 1);

-- if pass lesser number of columns than use colum name in insert statemnt above process will not works
insert into a_amazon_orders(order_id, order_date, product_name, total_price, payment_method, discount) values(1,'2022-10-02','Baby soap',130,'UPI', 1);
select * from a_amazon_orders;

-- Primary key constraints similar to Unique 
-- in Unique you have NULL, but primary key NULL not allowded
-- primary key is Unique constrinats + not Null constrinats together
-- primary key can be combination of two columns also it should be unique
-- Foreign key constraints
-- Multiple Unique key in table (Non clustered Index), Primary key only one in table (Clustered Index)

-- delete all data
delete from a_amazon_orders;
-- delete some specific data, delete with filter condition
delete from a_amazon_orders where order_id = 2; -- DML
-- go row by row and check and delete if matched delete the rows
-- where is a filter condition

--- Update -----
-- set discount to 10 for all columns
-- manupulating data - DML
update a_amazon_orders
set discount = 10

-- updating to specific columns
update a_amazon_orders
set discount = 10
where order_id = 2;

-- order or execution 
-- first go to table than go to where than set

-- updating two columns
update a_amazon_orders
set discount = 10, payment_method = 'UPI'
where order_id = 2;