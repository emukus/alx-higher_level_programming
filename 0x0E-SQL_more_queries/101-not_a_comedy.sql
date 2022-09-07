-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows sorted in ascending order by the show title
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- can use a maximum of two SELECT statement
SELECT s.title
FROM tv_shows s
WHERE s.title NOT IN (
	SELECT s.title
	FROM tv_shows s
	INNER JOIN tv_show_genres m ON s.id = m.show_id
	INNER JOIN tv_genres g ON m.genre_id = g.id
	WHERE g.name = 'Comedy'
)
ORDER BY s.title ASC;
