---- Views
-- Table are physicall data
-- View can consider as Vitrual Tables
-- when creating view use order_vw which is good to know

create view order_vw as  -- eneveloping the query
select * from orders

-- Querying the View
select * from order_vw -- going to above view and run the query

-- view goes to defination and run the query, never create seperate table
-- data is in the original tables

-- defination of view
create view [dbo].[order_vw] as
select * from orders

-- why views are Importants, multiple advatages
-- some big query need to share to other, create a view and give the view name
-- select * from orders, security of colum name, seperate regional manger, only 
-- want to share the regional data, create view

-- Referntial Intergirity constants -- reference
select * from employee
select * from department;
-- restict emplyee from departments
-- emplyee table coum refer to dept table, FK

create table emp
(
  emp_id integer,
  emp_name varchar(20),
  dep_id int reference dept(dept_id)
  -- dept_id should be primary key 
)
