function weather() {
  var sound = new Audio('hangouts_call.mp3');
  var location = document.getElementById("location");
  var apiKey = "1556cb41bdce6b830c27a0d25748ceb0";
  var url = "https://api.darksky.net/forecast/";

  navigator.geolocation.getCurrentPosition(success, error);

  function success(position) {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;

    $.getJSON(
      url + apiKey + "/" + latitude + "," + longitude + "?callback=?",
      function(data) {
        $("#temp").html(data.currently.temperature + "° F");
        $("#minutely").html(data.minutely.summary);
      }
    );
  }

  function error() {
    var i = 0;
    location.innerHTML = "Unable to retrieve your location";
    sound.play();
  }

  location.innerHTML = "Locating...";
}

weather();
