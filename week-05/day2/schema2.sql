
DROP TABLE if exists customers CASCADE;
CREATE TABLE customers (
  id int PRIMARY KEY,
  customer_name varchar(255),
  address_id int REFERENCES addresses(id)
);

DROP TABLE if exists orders CASCADE;
CREATE TABLE orders (
  id int PRIMARY KEY,
  customer_id int REFERENCES customers(id),
  item_quantity int 
);

DROP TABLE if exists product_orders CASCADE;
CREATE TABLE product_orders (
  id int PRIMARY KEY,
  order_id int REFERENCES orders(id),
  product_id int REFERENCES products(id),
  total int 
);

DROP TABLE if exists products CASCADE;
CREATE TABLE products (
  id int PRIMARY KEY,
  product_name varchar(200),
  item_price int
);

DROP TABLE if exists addresses CASCADE;
CREATE TABLE addresses (
  id int PRIMARY KEY,
  line_1 varchar(255),
  city varchar(255),
  state varchar(255),
  zipcode varchar(255)
);

