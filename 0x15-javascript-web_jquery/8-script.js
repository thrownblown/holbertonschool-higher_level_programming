$(document).ready(function () {
  const url = 'https://swapi.co/api/films/';
  $.get(url, function (data) {
    for (let movie of data.results) {
      let li = '<li>' + movie.title + '</li>';
      $('#list_movies').append(li);
    }
  });
});
