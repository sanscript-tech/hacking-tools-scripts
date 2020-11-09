function clock(){
	// Getting Time
	let now = new Date()
	let hours = now.getHours()
	let min = now.getMinutes()
	let seconds = now.getSeconds()
	hours = (hours < 10) ? `0${hours}` : hours
	min = (min < 10) ? `0${min}` : min
	seconds = (seconds < 10) ? `0${seconds}` : seconds
	if(hours > 12){
		document.getElementById('digitalClock').innerHTML = `${hours%12}:${min}:${seconds} PM`
	}
	else
		document.getElementById('digitalClock').innerHTML = `${hours}:${min}:${seconds} AM`
}
setInterval(clock, 1000)