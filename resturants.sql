drop database if exists fooddelivery;

create database shops;
use shops;

create table listofshops(
id int primary key,
name varchar(50)

);

insert into listofshops
(id,name)
values 
(1,"food court"),
(2,"hangy & swigy"),
(3,"buddy's bites"),
(4,"dc cafe"),
(5,"enzo"),
(6,"one food world"),
(7,"arasan"),
(8,"darling canteen"),
(9,"quick bytes");