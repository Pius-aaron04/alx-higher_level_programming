-- list tv shows by by their genre
SELECT title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, tv_show_genres.genre_id;
