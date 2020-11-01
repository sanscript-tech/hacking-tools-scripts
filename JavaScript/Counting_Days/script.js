// get the present time
var presentDate = new Date();
// mention the target time
var targetDate = new Date("Jan 21, 2021 00:00:00");
const oneDay = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
// days left
var days = Math.floor(Math.abs(targetDate - presentDate) / oneDay);
console.log("Days Left:" + days);
