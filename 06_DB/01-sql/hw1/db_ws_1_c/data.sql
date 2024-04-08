-- 1
SELECT genre, count(*) AS count, avg(duration) AS average_duration FROM songs GROUP BY genre;
