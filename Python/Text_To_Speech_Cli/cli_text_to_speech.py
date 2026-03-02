# Google Text to Speech API
from gtts import gTTS

# Input sentence from user
input_text = input("Enter a sentence in English: ")

#converting sentence to audio
tts = gTTS(text=input_text, lang='en')

# save the output in to an mp3 file
tts.save("output_audio.mp3")

print("Audio file saved successfully...")