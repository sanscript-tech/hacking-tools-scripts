const gTTS = require('gtts'); 
var readlineSync = require('readline-sync');
      
var text = readlineSync.question('Enter text');
var gtts = new gTTS(text, 'en'); 
  
gtts.save('Voice.mp3', function (err, result){ 
    if(err) { throw new Error(err); } 
    console.log("Text to speech converted!"); 
}); 