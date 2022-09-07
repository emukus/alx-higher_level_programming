-- Lists all Comedy shows in the database hbtn_0d_tvshows sorted in ascending order by the show title.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- You can use only one SELECT statement
SELECT tv_shows.title
FROM tv_shows
INNER JOIN tv_show_genres m ON tv_shows.id = m.show_id
INNER JOIN tv_genres g ON m.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY tv_shows.title ASC;
