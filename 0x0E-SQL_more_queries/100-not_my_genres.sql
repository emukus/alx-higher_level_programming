-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- must be sorted in ascending order by the genre name
-- can use a maximum of two SELECT statement
SELECT g.name
FROM tv_genres g
WHERE g.name NOT IN (
	SELECT g.name
	FROM tv_genres g
	INNER JOIN tv_show_genres m ON g.id = m.genre_id
	INNER JOIN tv_shows s ON m.show_id = s.id
	WHERE s.title = 'Dexter'
)
ORDER BY g.name ASC;
