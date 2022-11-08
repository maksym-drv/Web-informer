// nav
$('.navToggle').click(function () {
  $('body').toggleClass('navActive');
});

// ding
var ding = document.getElementById('ding');
var body = document.getElementById("body");
// var reply = document.getElementById("reply");
// var share = document.getElementById("share");
ding.addEventListener('show.bs.dropdown', function () {
  body.classList.add('dingActive');
});
ding.addEventListener('hidden.bs.dropdown', function () {
  body.classList.remove('dingActive');
});

function copyUrl(url, id) {
  navigator.clipboard.writeText(url);
  alert("Copied message #" + id + " url to clipboard");
}