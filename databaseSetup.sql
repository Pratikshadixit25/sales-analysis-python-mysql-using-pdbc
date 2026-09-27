CREATE DATABASE IF NOT EXISTS products;
USE products;

create table if not exists product(
			product_id int PRIMARY KEY AUTO_INCREMENT,
            product_name varchar(45),
            category varchar(30),
            price float,
            quantity_sold int,
            discount float,
            city varchar(30));
            
INSERT IGNORE INTO product
(product_id, product_name, category, price, quantity_sold, discount, city)
VALUES
(101, 'Laptop', 'Electronics', 55000, 12, 5, 'Pune'),
(102, 'Mouse', 'Electronics', 800, 50, 10, 'Mumbai'),
(103, 'Chair', 'Furniture', 4500, 20, 5, 'Pune'),
(104, 'Keyboard', 'Electronics', 1500, 35, 8, 'Nashik'),
(105, 'Table', 'Furniture', 7000, 15, 10, 'Mumbai');


CREATE TABLE IF NOT EXISTS product_analysis (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(45) UNIQUE,
    revenue FLOAT,
    discount_amount FLOAT,
    net_revenue FLOAT
);


