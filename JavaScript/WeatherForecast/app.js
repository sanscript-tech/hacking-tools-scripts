var temp = {
    key: "87cde31000e5170290cebdd94820d23d",
    base: "https://api.openweathermap.org/data/2.5/"
  }
var notificationElement = document.querySelector(".notification");
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(setPosition);
    notificationElement.innerHTML = "";

} 
else {
    notificationElement.innerHTML = "Geolocation is not supported by this browser.";
  }

function setPosition(position){
  let latitude = position.coords.latitude;
  let longitude = position.coords.longitude;
  
  getWeather(latitude, longitude);
}
  function getWeather(lat,lon) {
    fetch(`${temp.base}weather?lat=${lat}&lon=${lon}&units=metric&appid=${temp.key}`)
      .then(weather => {
        return weather.json();
      }).then(displayResults);
  }
 
  function displayResults (weather) {
    let city = document.querySelector('.location .city');
    city.innerText = `${weather.name}, ${weather.sys.country}`;
  
    let temp = document.querySelector('.current .temp');  
    temp.innerHTML =`${Math.round(weather.main.temp)}<span>°C</span>`

    let weather_el = document.querySelector('.current .weather');
    weather_el.innerText = weather.weather[0].main;
  
    let wind=document.querySelector('.wind-speed');
    wind.innerText=weather.wind.speed;

    let deg=document.querySelector('.wind-degree');
    deg.innerText=weather.wind.deg;

  }
  
 
  