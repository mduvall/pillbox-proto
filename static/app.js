function initApp() {
  var inputEl = document.querySelector("#search-field");

  inputEl.addEventListener("keyup", function(e) {
    var val = e.target.value,
        req = new XMLHttpRequest();

    req.open("GET", "/search/" + val, true);
    req.onreadystatechange = function() {
      var jsonRes;

      if (req.readyState !== 4 || req.status !== 200) {
        return;
      }

      document.querySelector("#pills-container").innerHTML = req.responseText;
    };
    req.send();
  });
}

document.addEventListener("DOMContentLoaded", initApp);