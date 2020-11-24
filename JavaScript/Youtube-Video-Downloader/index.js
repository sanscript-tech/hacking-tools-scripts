#!/usr/bin/env node
const fs = require('fs');
const readline = require('readline');
const ytdl = require('ytdl-core');
const chalk = require('chalk');
const figlet = require('figlet');
const args = process.argv;
// Download Function
download = (link) => {
	getTime = () => {
		let today = new Date();
		let y = today.getFullYear();
		let m = today.getMonth() + 1;
		let d = today.getDate();
		let h = today.getHours();
		let mi = today.getMinutes();
		let s = today.getSeconds();
		return y + "-" + m + "-" + d + "-" + h + "-" + mi + "-" + s;
	}
	console.log(chalk.cyan("Starting download..."));
	ytdl(link).once('response', () => {
		starttime = Date.now()
	}).on('progress', (chunkLength, downloaded, total) => {
		const percent = downloaded / total;
		readline.cursorTo(process.stdout, 0);
		process.stdout.write(`${(percent * 100).toFixed(2)}% downloaded `);
		process.stdout.write(`(Total Download Size : ${(total / 1024 / 1024).toFixed(2)}MB)\n`);
		readline.moveCursor(process.stdout, 0, -1);
	}).on('finish', () => {
		console.log(chalk.greenBright("\nSuccessfully Downloaded!"))
	}).pipe(fs.createWriteStream(`video-${getTime()}.mp4`))
}
// Help Command for User
help = () => {
	console.log(chalk.yellowBright(figlet.textSync("YouTube Downloader", function(err, data){
		if(err){
			console.log(err);
		}
		console.log(data);
	})))
	console.log(chalk.green(`Run ${chalk.yellow(`ytdload "<link-here>"`)} to download the youtube video`));
}
// If the user only enters ytdload
if(args.length == 2){
	help();
}else{
	// Getting the link entered by user
	const link = args[2];
	download(link);
}