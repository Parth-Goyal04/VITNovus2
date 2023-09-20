DROP DATABASE IF EXISTS shops;

create database pricing;
use pricing;


create table cost(
id INT primary key,
shop varchar(50),
destination varchar(50),
distance float,
distcharge int not null,
totalcharge int not null,
bill1k boolean
);

insert into cost
(id,shop,destination,distance,distcharge,totalcharge,bill1k)
values 
(1,"quick bites","q-block",100,10,10+10,false),
(2,"buddies and bites","q-block",10,10,10+10,false),
(3,"enzo","q-block",650,20,20+10,false),
(4,"hangy and swigy","q-block",850,30,10+30,false),
(5,"arasan","q-block",800,30,30+10,false),
(6,"one food world","q-block",850,30,30+10,false),
(7,"food court","q-block",1200,40,40+10,false),
(8,"dc canteen","q-block",1250,40,40+10,false),
(9,"dc cafe","q-block",1200,40,40+10,false),
(10,"quick bites","q-block",100,10,10+10+10,true),
(11,"buddies and bites","q-block",10,10,10+10+10,true),
(12,"enzo","q-block",650,20,20+10+10,true),
(13,"hangy and swigy","q-block",850,30,10+30+20,true),
(14,"arasan","q-block",800,30,30+10+20,true),
(15,"one food world","q-block",850,30,30+20,true),
(16,"food court","q-block",1200,40,40+10+20,true),
(17,"dc canteen","q-block",1250,40,40+10+20,true),
(18,"dc cafe","q-block",1200,40,40+10+20,true);

