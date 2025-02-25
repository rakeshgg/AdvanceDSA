

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

/*

CREATE TABLE [dbo].[returns] (
    [Order_Id]      NVARCHAR (50) NOT NULL,
    [Return_Reason] NVARCHAR (50) NOT NULL
);
*/

----- Multiple Tables ------
-- Joins
-- excel v lookup to do joins
-- alias given so database will know which order id to refer for this
-- joins always use aliases if using multiple columns in a table
-- joins can be done on anything not necessarly on relationship, join in non-primary as well

select o.Order_ID, o.Order_Date, r.Return_Reason
from superstore_orders as o
inner join returns as r on o.Order_ID = r.Order_ID;

-- all reslt from superstore_orders and returns
-- Order_ID is duplicate
select *
from superstore_orders as o
inner join returns as r on o.Order_ID = r.Order_ID;

-- remove duplicate Order_ID
select o.*, r.Return_Reason
from superstore_orders as o
inner join returns as r on o.Order_ID = r.Order_ID;

-- left joins - if no match than it will null in output table
-- if match than data
-- whatever there before left join is left table
-- get all record from left table and what ever match to right table will be available in output if not than it will be null
select o.Order_ID, o.Order_Date, r.Return_Reason, r.Order_ID
from superstore_orders as o
left join returns as r on o.Order_ID = r.Order_ID;

-- Important inner join, left join

-- all records/order not present in return tables
-- after from , join than where will executed
select o.Order_ID, o.Order_Date, r.Return_Reason, r.Order_ID
from superstore_orders as o
left join returns as r on o.Order_ID = r.Order_ID
where r.Order_ID is null;

-- how much sales i lost from the return
-- get null also
select r.Return_Reason, sum(Sales) as total_sales
from superstore_orders as o
left join returns as r on o.Order_ID = r.Order_ID
group by r.Return_Reason;

-- null not come
select r.Return_Reason, sum(Sales) as total_sales
from superstore_orders as o
inner join returns as r on o.Order_ID = r.Order_ID
group by r.Return_Reason;


-------- employee, dept Table ------
/*
create table employee(
    emp_id int,
    emp_name varchar(20),
    dept_id int,
    salary int,
    manager_id int,
    emp_age int
);
insert into employee values(1,'Ankit',100,10000,4,39);
insert into employee values(2,'Mohit',100,15000,5,48);
insert into employee values(3,'Vikas',100,10000,4,37);
insert into employee values(4,'Rohit',100,5000,2,16);
insert into employee values(5,'Mudit',200,12000,6,55);
insert into employee values(6,'Agam',200,12000,2,14);
insert into employee values(7,'Sanjay',200,9000,2,13);
insert into employee values(8,'Ashish',200,5000,2,12);
insert into employee values(9,'Mukesh',300,6000,6,51);
insert into employee values(10,'Rakesh',500,7000,6,50);
select * from employee;

create table dept(
    dep_id int,
    dep_name varchar(20)
);
insert into dept values(100,'Analytics');
insert into dept values(200,'IT');
insert into dept values(300,'HR');
insert into dept values(400,'Text Analytics');
*/

select * from employee;
select * from dept;

-- cross join
select * 
from employee, dept
order by employee.emp_id;

-- this is also cross join
-- 1=1 always true so cross join
-- each record of one table join with all other record of other table
select * 
from employee
inner join dept on 1=1
order by employee.emp_id;

-- inner join -- only matched from left table to right one
select e.emp_id, e.emp_name, e.dept_id, d.dep_name
from employee as e
inner join dept as d on e.dept_id = d.dep_id;

select e.emp_id, e.emp_name, e.dept_id, d.dep_name
from employee as e
left join dept as d on e.dept_id = d.dep_id;

-- right join, reverse of left join, get everything from right one and matched not matched  from left one
select e.emp_id, e.emp_name, e.dept_id, d.dep_name
from employee as e
right join dept as d on e.dept_id = d.dep_id;
-- same as swap table name
select e.emp_id, e.emp_name, e.dept_id, d.dep_name
from dept as d
left join employee as e on e.dept_id = d.dep_id
-- real word you dont required right join, you can swap table name use left join itself



---- Assignments ----
-- Note: please do not use any functions which are not taught in the class. you need to solve the questions only with the concepts that have been discussed so far.

-- 1- write a query to get region wise count of return orders
select region,count(distinct o.order_id) as no_of_return_orders
from orders o
inner join returns r on o.order_id=r.order_id
group by region

-- 2- write a query to get category wise sales of orders that were not returned
select category,sum(o.sales) as total_sales
from orders o
left join returns r on o.order_id=r.order_id
where r.order_id is null
group by category


-- 3- write a query to print dep name and average salary of employees in that dep .
select d.dep_name,avg(e.salary) as avg_sal
from employee e
inner join dept d on e.dept_id=d.dep_id
group by d.dep_name

-- 4- write a query to print dep names where none of the emplyees have same salary.
-- in dep no emplyee have same salary
select d.dep_name
from employee e
inner join dept d on e.dept_id=d.dep_id
group by d.dep_name
having count(e.emp_id)=count(distinct e.salary)
-- having count(distinct e.salary) = count(1)

-- 5- write a query to print sub categories where we have all 3 kinds of returns (others,bad quality,wrong items)
select o.sub_category
from orders o
inner join returns r on o.order_id=r.order_id
group by o.sub_category
having count(distinct r.return_reason)=3

-- 6- write a query to find cities where not even a single order was returned.
select city
from orders o
left join returns r on o.order_id=r.order_id
group by city
having count(r.order_id)=0

-- 7- write a query to find top 3 subcategories by sales of returned orders in east region
select top 3 sub_category,sum(o.sales) as return_sales
from orders o
inner join returns r on o.order_id=r.order_id
where o.region='East'
group by sub_category
order by return_sales  desc

-- 8- write a query to print dep name for which there is no employee
select d.dep_id,d.dep_name
from dept d 
left join employee e on e.dept_id=d.dep_id
group by d.dep_id,d.dep_name
having count(e.emp_id)=0;

-- 9- write a query to print employees name for which dep id is not avaiable in dept table
select e.*
from employee e 
left join dept d  on e.dept_id=d.dep_id
where d.dep_id is null;




