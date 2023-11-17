-- Lists shows by genre
SELECT title, tv_genres.name
FROM tv_shows ts
LEFT JOIN tv_show_genres tsg
ON ts.id = tsg.show_id
JOIN tv_genres ON tv_genres.id = tsg.genre_id
ORDER BY ts.title,tv_genres.name ASC;
