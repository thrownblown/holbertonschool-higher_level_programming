$(document).ready(function () {
    const url = 'https://swapi.co/api/people/5/';
    $.get(url, (data) => $('#character').html(data.name));
});
