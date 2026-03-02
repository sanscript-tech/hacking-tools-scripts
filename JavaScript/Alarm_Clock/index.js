const alarmSubmit = document.getElementById("alarmSubmit");
const alarmStop = document.getElementById("alarmStop");
const audio = document.getElementById("alarmAudio");

// Add an event listener to the submit button
alarmSubmit.addEventListener("click", setAlarm);

// Add an event listener to the stop button
alarmStop.addEventListener("click", stopAlarm);

// function to play the alarm ring tone
function ringBell() {
	audio.play();
}

// function to set alarm
function setAlarm(e) {
	e.preventDefault();
	const alarm = document.getElementById("alarm");
	alarmDate = new Date(alarm.value);
	now = new Date();
	console.log(now);
	let timeToAlarm = alarmDate - now;
	console.log(timeToAlarm);
	if (timeToAlarm >= 0) {
		setTimeout(() => {
			ringBell();
		}, timeToAlarm);
	}
}

// function to stop alarm
function stopAlarm(e) {
	audio.pause();
}
