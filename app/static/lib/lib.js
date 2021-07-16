function setCookie(cookie_name, value, days) {
  var exdate = new Date();
  exdate.setDate(exdate.getDate() + days);
  var cookie_value = escape(value) + ((days == null) ? '' : '; expires=' + exdate.toUTCString()); // days 안넣으면 만료일 없음
  document.cookie = cookie_name + '=' + cookie_value;
}
  
function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  // 조건에 맞는 쿠키가 없다면 undefined 반환
  return matches ? decodeURIComponent(matches[1]) : undefined;
}
  
function delCookie(name) {
  setCookie(name, 0, -1);
}

function format() { // 문자열 format 함수
  var args = Array.prototype.slice.call (arguments, 1);
  return arguments[0].replace (/\{(\d+)\}/g, function (match, index) {
     return args[index];
  });
}