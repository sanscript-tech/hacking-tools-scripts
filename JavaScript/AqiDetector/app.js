var temp = {
    key: "943422edf7ee41eb9b0ba3854e628f08	",
    base: "https://api.weatherbit.io/v2.0/current/airquality?"
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
    console.log(latitude);
    console.log(longitude);    
getAQI(latitude, longitude);
  }
function getAQI(lat,lon) {
      fetch(`${temp.base}lat=${lat}&lon=${lon}&units=metric&key=${temp.key}`)
        .then(aqi => {
          return aqi.json();
        }).then(displayResults);
}
function displayResults(aq){
    let aqi=document.querySelector(".aqi");
    aqi.innerHTML=`${aq.data[0].aqi}`;
    let location=document.querySelector(".location");
    location.innerHTML=`${aq.city_name},${aq.country_code}`
}