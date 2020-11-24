
var level=document.querySelector(".charging-level")
var status=document.querySelector(".status")
var charge=document.querySelector(".charge")
var discharge=document.querySelector(".discharge")

if(navigator.getBattery()){
navigator.getBattery()
    .then(function(battery) {
        level.innerHTML = battery.level*100;
        battery.onlevelchange=function()
        {
            level.innerHTML = battery.level*100;
        }
        charge.innerHTML=battery.chargingTime;
        battery.onchargingtimechange=function()
        {
            charge.innerHTML = battery.chargingTime;
        }
        discharge.innerHTML=battery.dischargingTime;
        battery.ondischargingtimechange=function()
        {
            discharge.innerHTML = battery.dischargingTime;
        }
        if(battery.charging==true) {status.innerHTML="Charging";
        battery.onchargingchange=function()
        {
            status.innerHTML="Not Charging";
        }}
        else {status.innerHTML="Not Charging";
        battery.onchargingchange=function()
        {
            status.innerHTML="Charging";
        }}
    })
    .catch(function(e) {
        console.error(e);
    });
}
else{
    status.innerHTML="Browser doesn't support ";
}