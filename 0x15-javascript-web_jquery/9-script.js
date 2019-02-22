$(document).ready(() => {
  const url = 'https://fourtonfish.com/hellosalut/?lang=';
  let lang = $('html').attr('lang');
  $.get(url + lang, (data) => $('#hello').html(data.hello));
});
