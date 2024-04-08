-- 1
SELECT * FROM users WHERE age >= 30 AND balance >= 1000;
-- 2
SELECT * FROM users WHERE age <= 20 AND balance <= 1000;
-- 3
SELECT * FROM users WHERE first_name LIKE "현%" AND country = "제주특별자치도" ORDER BY age DESC LIMIT 1;
-- 4
SELECT * FROM users WHERE last_name = "박" AND age >= 25 ORDER BY age LIMIT 1;
-- 5
SELECT * FROM users WHERE first_name IN ("재은", "영일") ORDER BY balance DESC LIMIT 1;
-- 6
SELECT * FROM users GROUP BY country HAVING balance = max(balance) ORDER BY balance DESC, country DESC;
-- 7
SELECT * FROM users WHERE age >= 30 AND balance >= (SELECT avg(balance) FROM users WHERE age >= 30);