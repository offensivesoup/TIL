-- 1
SELECT * FROM users WHERE first_name LIKE "하%";
-- 2
SELECT * FROM users WHERE phone LIKE "%555";
-- 3
SELECT * FROM users WHERE country LIKE "경상%";
-- 4
SELECT * FROM users WHERE country LIKE "경_남%" or country LIKE "충_남%";