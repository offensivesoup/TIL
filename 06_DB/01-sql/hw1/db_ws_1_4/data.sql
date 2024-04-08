-- 1
SELECT avg(age) AS average_age FROM users;
-- 2
SELECT country, count(*) AS user_count FROM users GROUP BY country;
-- 3
SELECT * FROM users WHERE balance = (SELECT max(balance) FROM users) LIMIT 1;
-- 4
SELECT country, avg(balance) FROM users GROUP BY country;
-- 5
SELECT (max(balance) - min(balance)) AS balance_difference FROM users;
