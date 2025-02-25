--- Select and Where

/*
CREATE TABLE [dbo].[superstore_orders] (
    [Row_ID]         SMALLINT       NOT NULL,
    [Order_ID]       NVARCHAR (50)  NOT NULL,
    [Order_Date]     DATETIME       NOT NULL,
    [Ship_Date]      DATETIME       NOT NULL,
    [Ship_Mode]      NVARCHAR (50)  NOT NULL,
    [Customer_ID]    NVARCHAR (50)  NOT NULL,
    [Customer_Name]  NVARCHAR (50)  NOT NULL,
    [Segment]        NVARCHAR (50)  NOT NULL,
    [Country_Region] NVARCHAR (50)  NOT NULL,
    [City]           NVARCHAR (50)  NOT NULL,
    [State]          NVARCHAR (50)  NOT NULL,
    [Postal_Code]    INT            NULL,
    [Region]         NVARCHAR (50)  NOT NULL,
    [Product_ID]     NVARCHAR (50)  NOT NULL,
    [Category]       NVARCHAR (50)  NOT NULL,
    [Sub_Category]   NVARCHAR (50)  NOT NULL,
    [Product_Name]   NVARCHAR (150) NOT NULL,
    [Sales]          FLOAT (53)     NOT NULL,
    [Quantity]       TINYINT        NOT NULL,
    [Discount]       FLOAT (53)     NOT NULL,
    [Profit]         FLOAT (53)     NOT NULL
);
*/

-- where filter happens row by row

select top 10 Order_ID, Order_Date
from superstore_orders
order by Order_Date asc;

-- order pf execution
-- from (which table to get date), order by than top 2 

-- to get distinct value of columns
select distinct Ship_Mode from superstore_orders;
select distinct Order_Date from superstore_orders;

select * from superstore_orders;

select distinct Ship_Mode, Segment from superstore_orders;

-- Filters in one columns ---
select * from superstore_orders
where Ship_Mode = 'First Class';

select * from superstore_orders
where Order_Date = '2020-12-8';

select top 5 Order_Date, Quantity from superstore_orders
where Quantity >= 5
order by Quantity desc;
-- order of execution
-- from - go to table, where - apply filter, than order by than select top 5 and return

-- Range between
select * from superstore_orders
-- boundary dates also includes inclusive []
where Order_Date between '2020-12-8' and'2020-12-10'
order by Order_Date desc;

-- Multiple value give in (), not in ()
-- if single value given than = 
select distinct Ship_Mode from superstore_orders
where Ship_Mode in ('First Class', 'Same Day');

select * from superstore_orders
where Quantity in (3, 4, 5)
order by Quantity;

select distinct Ship_Mode from superstore_orders
where Ship_Mode not in ('First Class', 'Same Day');

-- how >, < is used in string - using ascii value
select distinct Ship_Mode from superstore_orders
where Ship_Mode > 'First Class';

-- Filters on Multiple Columns ---
-- and both condition satisfied
select Order_Date, Ship_Mode, Segment from superstore_orders
where Ship_Mode = 'First Class' AND Segment = 'Consumer';
-- if one condition satisfied
-- db first check Ship_Mode is valid than dont check 2nd one, if 1st condition not statisifed than check 2nd one 
select Order_Date, Ship_Mode, Segment from superstore_orders
where Ship_Mode = 'First Class' or Segment = 'Consumer';

-- in clause same as Ship_Mode in ('First Class', 'Same Day');
-- where is purely row wise
select Ship_Mode, Order_Date from superstore_orders
where Ship_Mode = 'First Class' or Ship_Mode = 'Same Day';

-- or will always incrses the rows, and will decrese the rows
select * from superstore_orders
where Quantity > 5 AND Order_Date < '2020-11-08';

-- create new columns in outputs, any arthetics, string funct can be put here
-- getdate() -- current date and time
select *, Profit/Sales as ratio, Profit + Sales as total, getdate() as Currentdate
from superstore_orders;

-- Pattern matching like operator
select Order_ID, Order_Date, Customer_Name
from superstore_orders
where Customer_Name = 'Clarie Gute';

-- after c anything
-- customer name starting with C
select Order_ID, Order_Date, Customer_Name
from superstore_orders
where Customer_Name like 'C%';

-- end with Schild
select Order_ID, Order_Date, Customer_Name
from superstore_orders
where Customer_Name like '%Schild';

-- ven in between
select Order_ID, Order_Date, Customer_Name
from superstore_orders
where Customer_Name like '%ven%';

-- SQL server by default case insestive
-- case insestive search, convert all in cap so its insestive search
select Order_ID, Order_Date, upper(Customer_Name) as name_upper
from superstore_orders
where upper(Customer_Name) like 'A%A';

-- _ means one char, underscore
select Order_ID, Order_Date, upper(Customer_Name) as name_upper
from superstore_orders
where upper(Customer_Name) like '_A%';

-- [] -- any of char in square brackets
select Order_ID, Order_Date, upper(Customer_Name) as name_upper
from superstore_orders
where upper(Customer_Name) like 'c[albo]%';

-- 2nd char canntot be albo use ^(negate)
select Order_ID, Order_Date, upper(Customer_Name) as name_upper
from superstore_orders
where upper(Customer_Name) like 'c[^albo]%';

-- Range [a-h]
select Order_ID, Order_Date, upper(Customer_Name) as name_upper
from superstore_orders
where upper(Customer_Name) like 'c[a-h]%';

/*
   order of execution
   from, where, select * , order by, top 5
   so its possible to apply order by on select *
*/
select top 5 * , Profit/Sales as ratio
from superstore_orders
where Cateogory = 'Furniture'
order by ratio

-- Filtering null values -- use is operator
-- null if on creation no value is supplied for some fields than defualt is null
-- null is not comparable with any other
select * from superstore_orders
where City is NULL

select * from superstore_orders
where City is not NULL;