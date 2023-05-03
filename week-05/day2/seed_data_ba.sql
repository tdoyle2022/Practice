INSERT INTO delivery_address(id, line_1, city, state, zipcode) VALUES (2, '6232 Guiseppe Courts', 'Jamartown', 'Maryland', '49028');
INSERT INTO delivery_address(id, line_1, city, state, zipcode) VALUES (3, '6232 valley street', 'Jamestown', 'Virginia', '20033');

INSERT INTO users(id, first_name, last_name, credit_card, address_id, service_plan_id) VALUES (1, 'Darren', 'Berg', 2341, 1, 1);
INSERT INTO users(id, first_name, last_name, credit_card, address_id, service_plan_id) VALUES (2, 'Terry', 'Doyle', 2341, 2, 2);

INSERT INTO orders(id, customer_id, recipe_id) VALUES (1, 1, 1);
INSERT INTO orders(id, customer_id, recipe_id) VALUES (2, 2, 2);

INSERT INTO service_plans(id, daily, weekly, monthly) VALUES (1, NULL, 1, NULL);
INSERT INTO service_plans(id, daily, weekly, monthly) VALUES (2, NULL, NULL, 1);

INSERT INTO recipes(id, chicken, beef, fish, pork) VALUES (1, 'chicken', 'beef', 'fish', 'pork');
INSERT INTO recipes(id, chicken, beef, fish, pork) VALUES (2, 'chicken', 'beef', 'fish', 'pork');


