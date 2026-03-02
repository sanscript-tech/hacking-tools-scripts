const merge = require('easy-pdf-merge')
const args = process.argv
if(args.length === 2 || args.length === 3){
	console.log("Enter the path of two PDFs you want to merge!")
}else{
	merge([`${args[2]}`, `${args[3]}`], 'Merged-PDF.pdf', function(err){
		if(err)
			console.log(err)
		console.log("Merged Successfully!")
	})
}