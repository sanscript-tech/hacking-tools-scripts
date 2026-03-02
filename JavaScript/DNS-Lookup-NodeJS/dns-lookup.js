// Inbuilt NodeJS DNS Module
const dns = require('dns')
// To get user input
const readline = require('readline')
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
})
rl.question("Enter the URL or IP Address : ", (url) => {
	const options = {
		all: true,
	}
	dns.lookup(url, options, (err, addresses) => {
		if(err)
			console.log(err)
		if(addresses.length > 1){
			console.log(`IPv4 Address : ${addresses[0].address}`)
			console.log(`IPv6 Address : ${addresses[1].address}`)
		}else{
			if(addresses[0].family === 4)
				console.log(`IPv4 Address : ${addresses[0].address}`)
			else
				console.log(`IPv6 Address : ${addresses[0].address}`)
		}
	})
	rl.close()
})