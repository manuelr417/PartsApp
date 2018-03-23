-- This file contains the definitions of the tables used in the application.
--
-- Part table
create table parts(pid serial primary key, pname varchar(20), pmaterial varchar(10), pcolor varchar(10), pprice float);

-- Supplier table
create table supplier(sid serial primary key, sname varchar(10), scity varchar(10), sphone varchar(10));

-- Supplies table
create table supplies(pid integer references Parts(pid), sid integer references
Supplier(sid), qty integer, primary key(pid, sid));

-- PartSales table
create table partsales(psaleid serial primary key, pid integer references Parts(pid),
sid integer references Supplier(sid), sqty integer, sprice float, sdate Date);
