-- List all genres from 'hbtn_0d_tvshows' and display number of shows linked to each
-- Each record displays tv_genres.name, number of shows
-- Don't display a genre that doesn't have any shows linked
-- Results are sorted in descending order by the number of shows linked
SELECT tv_genres.name AS genre, COUNT(*) AS number_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
