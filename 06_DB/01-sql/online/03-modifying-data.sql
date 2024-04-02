-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');

CREATE TABLE articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    createdAt DATE NOT NULL
);

-- 1. Insert data into table

INSERT INTO articles (title, content, createdAt) VALUES ("hello" , "world", "2000-01-01");
INSERT INTO articles (title, content, createdAt) VALUES ("hello" , "DB", "2024-04-02");
INSERT INTO articles (title, content, createdAt) VALUES ("hello" , "world", "2000-01-01"), ("hello" , "world", "2000-01-02"), ("hello" , "world", "2000-01-03"), ("hello" , "world", "2000-01-04");
SELECT * FROM articles;
-- 2. Update data in table

UPDATE articles SET title = "update_title" WHERE id = 1;
-- 동시에도 가능하다.
UPDATE articles SET title = "update_title" , content = "update Content" WHERE id = 2;
UPDATE articles SET title = "JavaScript" , content = "not started" WHERE title = "hello";

-- 3. Delete data from table
DELETE FROM articles WHERE id = 6;
-- 테이블에서 작성일이 오래된 순으로 order by한후, 레코드 삭제
DELETE FROM articles WHERE id IN (SELECT id FROM articles ORDER BY createdAt LIMIT 2);
