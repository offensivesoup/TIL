CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    date DATE NOT NULL,
    myreal REAL NOT NULL
);

INSERT INTO orders(date, myreal) VALUES ("2000-01-01", 22.22);
INSERT INTO orders(date, myreal) VALUES ("2000-01-02", 33.33);
INSERT INTO orders(date, myreal) VALUES ("2000-01-03", 44.44);

CREATE TABLE customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    email VARCHAR(50),
    phone VARCHAR(50)
);

INSERT INTO customers(name, email, phone) VALUES ("허균", "hong@mial.com", '010-1234-1521');
INSERT INTO customers(name, email, phone) VALUES ("허균2", "hong@mial.com2", '010-1235-1521');
INSERT INTO customers(name, email, phone) VALUES ("허균3", "hong@mial.com3", '010-1236-1521');

DELETE FROM orders WHERE order_id = 3;
UPDATE customers SET name = "홍길동" WHERE customer_id = 1;

SELECT * FROM orders;
SELECT * FROM customers;