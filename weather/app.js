function weather() {
  var sound = new Audio('http://thepotatoplace.ga/');
  var location = document.getElementById("location");
  var apiKey = "23bc5a73297ae0b4f0f2aa05de4f1ba0";
  var url = "https://api.forecast.io/forecast/";
  function null_a(){
    return false;
  }

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
    location.innerHTML = "Unable to retrieve your location";
    while(1 == 1){
      sound.play();
      setTimeout(null_a(),500);
    }
  }

  location.innerHTML = "Locating...";
}

weather();
