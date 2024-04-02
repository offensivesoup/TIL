-- 1
SELECT * FROM tracks WHERE Name LIKE "%love%";
-- 2
SELECT * FROM tracks WHERE GenreId = 1 AND Milliseconds >= 300000;
-- 3
SELECT GenreId, Count(*) FROM tracks GROUP BY GenreId;
-- 4
SELECT GenreId, Sum(UnitPrice) AS TotalPrice FROM tracks GROUP BY GenreId HAVING TotalPrice >= 100;
