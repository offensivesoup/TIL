CREATE TABLE songs(
    id INTEGER PRIMARY KEY,
    title TEXT,
    artist TEXT,
    album TEXT,
    genre TEXT,
    duration INTEGER
);

PRAGMA table_info('songs');
SELECT * FROM songs;

-- 1

INSERT INTO songs (title, artist, album, genre, duration)
VALUES ("제목1" , "아이유" , "1집" , "팝", "100"),
        ("제목2" , "아이유" , "2집" , "팝", "200"),
        ("제목3" , "아이유" , "3집" , "팝", "300"),
        ("제목4" , "아이유" , "4집" , "팝", "400"),
        ("제목5" , "아이유" , "5집" , "팝", "500");
-- 2

UPDATE songs SET title = "New_title" WHERE id = 1;