-- Lists all shows from hbtn_0d_tvshows_rate by their rating sorted in descending order by the rating.
-- Each record should display: tv_shows.title - rating sum
-- can use only one SELECT statement
SELECT s.title, SUM(r.rate) AS rating
FROM tv_shows s
INNER JOIN tv_show_ratings r ON s.id = r.show_id
GROUP BY r.show_id
ORDER BY rating DESC;
