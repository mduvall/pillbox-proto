function initApp() {
  var inputEl = document.querySelector("#search-field"),
      sending = false,
      keyupTimeout;

  inputEl.addEventListener("keyup", function(e) {
    if (!keyupTimeout) {
      keyupTimeout = setTimeout(function() {
        var val = e.target.value,
            req = new XMLHttpRequest();

        if (val !== "") {
          req.open("GET", "/search/" + val, true);
          req.onreadystatechange = function() {
            keyupTimeout = null;
            if (req.readyState !== 4 || req.status !== 200) {
              return;
            }

            var pillContainerEl = document.querySelector("#pills-container");
            pillContainerEl.innerHTML = req.responseText;
          };
          req.send();
        } else {
          keyupTimeout = null;
        }
      }, 100);
    }

  });
}

document.addEventListener("DOMContentLoaded", initApp);