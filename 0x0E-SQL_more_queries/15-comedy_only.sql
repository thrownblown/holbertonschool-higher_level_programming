-- prints all the comedys
SELECT tv_shows.title FROM tv_shows, tv_genres, tv_show_genres WHERE tv_genres.name="Comedy" AND tv_genres.id = tv_show_genres.genre_id AND tv_shows.id=tv_show_genres.show_id ORDER BY tv_shows.title ASC;
