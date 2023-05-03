INSERT INTO addresses(id, line_1, city, state, zipcode) VALUES (2, '6232 Guiseppe Courts', 'Jamartown', 'Maryland', '49028');
INSERT INTO addresses(id, line_1, city, state, zipcode) VALUES (3, '6232 valley street', 'Jamestown', 'Virginia', '20033');

INSERT INTO customers(id, customer_name, address_id) VALUES (2, 'Darren Berg', NULL);
INSERT INTO customers(id, customer_name, address_id) VALUES(3, 'Tom Jerry', NULL)

INSERT INTO orders(id, customer_id, item_quantity) VALUES (3, 3, 3);
INSERT INTO orders(id, customer_id, item_quantity) VALUES (2, 2, 1);

INSERT INTO products(id, product_name, item_price) VALUES (1, 'chips', 1);
INSERT INTO products(id, product_name, item_price) VALUES (2, 'crackers', 2);

INSERT INTO product_orders(id, order_id, product_id, total) VALUES (3, 3, 3, 3);
INSERT INTO product_orders(id, order_id, product_id, total) VALUES (2, 2, 2, 2);