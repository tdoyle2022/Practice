DROP TABLE if exists users CASCADE;
CREATE TABLE users (
    id int PRIMARY KEY,
    first_name varchar(255),
    last_name varchar(255),
    credit_card int,
    address_id int REFERENCES delivery_address (id),
    service_plan_id int REFERENCES service_plans (id)
    
);

DROP TABLE if exists orders CASCADE;
CREATE TABLE orders (
  id int PRIMARY KEY,
  customer_id int REFERENCES users(id),
  recipe_id int REFERENCES recipes(id)
  
);

DROP TABLE if exists service_plans CASCADE;
CREATE TABLE service_plans (
  id      int PRIMARY KEY,
  daily   int,
  weekly  int,
  monthly int
);

DROP TABLE if exists recipes CASCADE;
CREATE TABLE recipes (
  id int PRIMARY KEY,
  chicken varchar(255),
  beef varchar(255),
  fish varchar(255),
  pork varchar(255)
);

DROP TABLE if exists delivery_address CASCADE;
CREATE TABLE delivery_address (
    id int PRIMARY KEY,
    line_1 varchar(255),
    city varchar(255),
    state varchar(255),
    zipcode varchar(255)
);

