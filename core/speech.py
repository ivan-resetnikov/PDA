# speech recongition
from vosk    import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16
# text to speech
from pyttsx3 import init
# fuzzy speech supression
from fuzzywuzzy import fuzz



# text to speech
tts = init()

# fuzzy speech suppresion
ratio = fuzz.ratio
tokenRatio = fuzz.token_set_ratio

# speech to text
print('Initializing speech recognizer (Vosk)'.center(50, '='))
recognizer = KaldiRecognizer(Model('./core/vosk-model-small-en-us-0.15'), 16000)
print('Speech recognizer initialized'.center(50, '='))

mic = PyAudio()
stt = mic.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)



def say (text:str) -> None :
	print(f'PDA: {text}')

	if tts._inLoop: tts.endLoop()

	tts.say(text)
	tts.runAndWait()


def setVoice (voice:str) -> None :
	voices = {
		'male' : 0,
		'female' : 1
	}

	tts.setProperty('voice', tts.getProperty('voices')[voices[voice]].id)


def setRate (rate: int) -> None :
	tts.setProperty('rate', rate)


def recognize (enableLower=True) :
	text = ''

	stt.start_stream()

	while True :
		data = stt.read(4096, exception_on_overflow = False)

		if recognizer.AcceptWaveform(data):
			text = recognizer.Result()

			text = f'{text[14:-3]}'

			if text :
				print(f'You: {text}')
				if enableLower : return text.lower()

				else : return text

	stt.stop()