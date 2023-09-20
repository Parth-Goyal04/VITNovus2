CREATE DATABASE fooddelivery;
use fooddelivery;

CREATE TABLE foodcourt(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20
);

INSERT INTO foodcourt
(id,itemname,price)
VALUES
(1,"curd + vada",25),
(2,"plain dosa",36),
(3,"veg biryani",43),
(4,"chicken biryani",93),
(5,"veg soup",43),
(6,"paneer tikka",115),
(7,"chicken tikka", 103),
(8,"bread",23),
(9,"kadai veg",68),
(10,"matter paneer",73),
(11,"butter chicken masala",108),
(12,"kadai chicken",113),
(13,"veg fried rice",73),
(14,"veg noodles",63),
(15,"manchurian", 98);

CREATE TABLE quickbites(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);

INSERT INTO quickbites
(id,itemname,price)
VALUES
(1,"choco brownies",40),
(2,"sandwich",25),
(3,"hot dog",80),
(4,"burger",100),
(5,"fried paneer sub",120),
(6,"veg pizza",80),
(7, "tea",20),
(8,"caramel pudding",50),
(9,"bombay vada pav",50),
(10,"lemonade",30),
(11,"coffee",30),
(12,"goli soda",35),
(13,"cold chocolate",30),
(14,"chicken tikka", 103),
(15,"choco chip cookies",23);

CREATE TABLE enzo(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);
INSERT INTO enzo
(id,itemname,price)
VALUES
(1,"choco brownies",50),
(2,"sandwich",40),
(3,"hot dog",80),
(4,"chicken burger",120),
(5,"chicken lolipop",120),
(6,"pizza",80),
(7, "maggie pack of 4",80),
(8,"bread",23),
(9,"kadai veg",68),
(10,"matter paneer",73),
(11,"butter chicken masala",108),
(12,"kadai chicken",113),
(13,"veg fried rice",73),
(14,"veg noodles",63),
(15,"manchurian", 98);


CREATE TABLE dccafe(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);

INSERT INTO dccafe
(id,itemname,price)
VALUES
(1,"1/2kg vanilla cake",225),
(2,"1/2kg black forest",275),
(3,"1/2kg white forest",295),
(4,"1kg choclate truffle",495),
(5,"1kg strawberry",495),
(6,"1kg mango",495),
(7, "1kg butterscotch",495);

CREATE TABLE buddysbites(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);
INSERT INTO buddysbites
(id,itemname,price)
VALUES
(1,"choco brownies",50),
(2,"sandwich",30),
(3,"burger",45),
(4,"cheese burger",60),
(5,"chips/snacks",20),
(6,"pizza",80),
(7, "cold drinks",40),
(8,"masala double omelette",40),
(9,"bread omelette",50),
(10,"aloo tikki slider ",45),
(11,"mayo sandwich",45),
(12,"bombay sandwich", 55),
(13,"veg fried rice",73),
(14,"veg noodles",63),
(15,"manchurian", 98);


CREATE TABLE dccanteen(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);

INSERT INTO dccanteen
(id,itemname,price)
VALUES
(1,"curd + vada",25),
(2,"plain dosa",36),
(3,"veg biryani",43),
(4,"chicken biryani",93),
(5,"veg soup",43),
(6,"paneer tikka",115),
(7,"chicken tikka", 103),
(8,"bread",23),
(9,"kadai veg",68),
(10,"matter paneer",73),
(11,"butter chicken masala",108),
(12,"kadai chicken",113),
(13,"veg fried rice",73),
(14,"veg noodles",63),
(15,"manchurian", 98);

 
CREATE TABLE hangyandswig(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);

INSERT INTO hangyandswig
(id,itemname,price)
VALUES
(1,"maggie",39),
(2,"maska bun",35),
(3,"masala double omelette",40),
(4,"bread omelette",50),
(5,"aloo tikki slider ",45),
(6,"mayo sandwich",45),
(7,"bombay sandwich", 55),
(8,"spring roll",59),
(9,"paneer roll",80),
(10,"chicken roll",80),
(11,"veg tikki wrap",85),
(12,"fried chicken wrap",125),
(13,"pasta ",99),
(14,"paneer sub",145),
(15,"special wings", 159);


CREATE TABLE arasan(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);


INSERT INTO arasan
(id,itemname,price)
VALUES
(1,"curd + vada",25),
(2,"plain dosa",36),
(3,"veg biryani",43),
(4,"chicken biryani",93),
(5,"veg soup",43),
(6,"paneer tikka",115),
(7,"chicken tikka", 103),
(8,"bread",23),
(9,"choco brownies",50),
(10,"sandwich",30),
(11,"burger",45),
(12,"cheese burger",60),
(13,"chips/snacks",20),
(14,"pizza",80),
(15, "cold drinks",40);

CREATE TABLE onefoodworld(
id INT PRIMARY KEY,
itemname VARCHAR(50),
price INT DEFAULT 20

);

INSERT INTO onefoodworld
(id,itemname,price)
VALUES
(1,"mexican veg corn panini",99),
(2,"arabian chicken panini",125),
(3,"red sauce pasta",99),
(4,"white sauce pasta",99),
(5,"veg soup",43),
(6,"crispy chicken popcorn",99),
(7,"crispy chicken strips(3pc)", 115),
(8,"spicy korean veg pops",89),
(9,"smoked BBQ veg pops",139),
(10,"spicy crispy corn",75),
(11,"chilli cheese toast",89),
(12,"cheese burger",60),
(13,"cheese garlic bread",135),
(14,"dragon shawarma roll",110),
(15, "dragon shawarma plate",150);

