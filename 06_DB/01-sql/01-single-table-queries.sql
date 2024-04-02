-- 01. Querying data

--  기본 구조
SELECT LastName FROM employees;

--  여러개 가져오기
SELECT LastName, FirstName FROM employees;

-- 전부 가져오기
SELECT * FROM employees;

-- 이름으로 가져오기
SELECT FirstName AS "이름" FROM employees; 

-- 단위를 바꿔서 가져오기
SELECT Name, Milliseconds / 60000 AS "재생 시간(분)" FROM tracks;

-- 02. Sorting data

-- 오름차순
-- ASC는 생략 가능

SELECT FirstName FROM employees ORDER BY FirstName ASC;

-- 내림차순

SELECT FirstName FROM employees ORDER BY FirstName DESC;

-- Country 기준으로 내림차순, City 기준 오름차순 정렬
-- Country 기준으로 정렬된 채, 그 안에서 City 기준으로 정렬된다.

SELECT Country, City FROM customers ORDER BY Country DESC, City ASC;

-- 정렬과 단위 변경 동시에

SELECT Name, Milliseconds / 60000 AS '재생 시간(분)' FROM tracks ORDER BY Milliseconds DESC;

-- 정렬에서 NULL 이 존재한다면, NULL 이 먼저 출력된다
-- NULL 정렬 예시

SELECT ReportsTo FROM employees ORDER BY ReportsTo;

-- 03. Filtering data

-- DISTINC 중복값 제거
SELECT DISTINCT Country FROM customers ORDER BY Country;

-- WHERE 조건 주기
SELECT LastName, FirstName, City FROM customers WHERE City = "Prague";
SELECT LastName, FirstName, City FROM customers WHERE City != "Prague";
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company IS NULL AND Country = "USA";
SELECT LastName, FirstName, Company, Country FROM customers WHERE Company IS NULL OR Country = "USA";
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 10000 AND 500000;
SELECT Name, Bytes FROM tracks WHERE Bytes >= 10000 AND Bytes <= 500000;
SELECT Name, Bytes FROM tracks WHERE Bytes BETWEEN 10000 AND 500000 ORDER BY Bytes; 
SELECT LastName, FirstName, Country FROM customers WHERE Country IN ("Canada", "Germany", "France");
SELECT LastName, FirstName, Country FROM customers WHERE Country NOT IN ("Canada", "Germany", "France");
-- 끝이 정해진 문자
SELECT LastName, FirstName FROM customers WHERE LastName LIKE "%son";
-- 몇글자인지 정확하게 정해짐
SELECT LastName, FirstName FROM customers WHERE FirstName LIKE "___a";
-- LIMIT을 거는것 : 나오는 개수 설정, ORDER BY 이후 사용
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 7;
-- LIMIT 앞에는 OFFSET 4개부터 7까지 나타냄
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 3, 4;
SELECT TrackId, Name, Bytes FROM tracks ORDER BY Bytes DESC LIMIT 4 OFFSET 3;

-- 04. Grouping data

-- 저절로 중복 제거가 된다. == DISTINCT 랑 같다.
SELECT Country FROM customers GROUP BY Country;
-- 집계함수에 대한 결과를 컬럼으로 사용할 수 있다는 점이 다르다.
SELECT Country, COUNT(*) FROM customers GROUP BY Country;
SELECT Composer, AVG(Bytes) FROM tracks GROUP BY Composer ORDER BY AVG(Bytes) DESC;
-- WHERE 절이 아닌, HAVING 조건이 필요하다 (집계함수에 대한 조건)
SELECT Composer, AVG(Milliseconds/60000) AS avgOfMinute FROM tracks GROUP BY Composer HAVING avgOfMinute < 10;
