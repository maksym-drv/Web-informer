// nav
$('.navToggle').click(function () {
  $('body').toggleClass('navActive');
});

// ding
var ding = document.getElementById('ding');
var body = document.getElementById("body");

ding.addEventListener('show.bs.dropdown', function () {
  body.classList.add('dingActive');
});
ding.addEventListener('hidden.bs.dropdown', function () {
  body.classList.remove('dingActive');
});

function copyUrl(url, id, type) {
  navigator.clipboard.writeText(url);
  alert("Copied " + type + " #" + id + " url to clipboard");
}

function replyMessage(id) {
  var reply_box = document.getElementById(id).getElementsByClassName('forumPost__reply--message')[0];
  if (reply_box.style.display == "block") { 
    var replies = document.getElementsByClassName("forumPost__reply--message");
    for(var i = 0; i < replies.length; i++){
      replies[i].style.display = "none";
    }
  } else {
    reply_box.style.display = "block";
  }
}