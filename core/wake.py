from datetime import datetime
from os       import system

import core.data   as database
import core.speech as speech
import core.const  as const



def wakeLoop () :
	print(' Entered wake loop '.center(50, '='))

	while True :
		speech.say('I\'m listening')
		command = speech.recognize()



		if speech.tokenRatio('access database', command) > 60:
			if 'remote' in command :
				pleased = False

				while not pleased :
					speech.say('Say remote database entry')
					pleased = database.accessRemoteDatabase(speech.recognize())

			elif 'local' in command :
				database.accessLocalDatabase()


		elif speech.ratio(command, 'create database and three') > 40:
			database.createDatabaseEntry()


		elif speech.ratio(command, 'open youtube') > 60:
			system('start https://youtube.com/')


		elif speech.ratio(command, 'search something') > 60:
			speech.say('Say your entry:')
			system('start https://duckduckgo.com/?q=' + '+'.join(speech.recognize().split()))


		elif speech.tokenRatio(command, 'what is it') > 55:
			if 'time' in command :
				time = datetime.now()
				speech.say('{}:{}'.format(str(time.hour).rjust(2, 'O'), str(time.minute).rjust(2, 'O')))

			elif 'date' in command :
				time = datetime.now()
				speech.say(time.strftime("%B %d, %Y"))


		elif speech.ratio(command, 'open games list') > 60:
			system('start D:/Main/Games')


		elif speech.ratio(command, 'thanks') > 60:
			speech.say('You are welcome :)')


		elif speech.ratio(command, 'how do i look') > 60:
			system('start microsoft.windows.camera:')
			speech.say('In my opinion, you look flabbergasting!')


		elif speech.ratio(command, 'stop') > 60 or \
			 speech.ratio(command, 'that\'s all') > 60 or \
			 speech.ratio(command, 'that is it') > 60 or \
			 speech.ratio(command, 'enter hybernation mode') > 60 or \
			 speech.ratio(command, 'start hybernation') > 60 or \
			 speech.ratio(command, 'sleep') > 60 :

			speech.say(f'Hybernating. say "open {const.name}" again, to start interaction')
			print(' Entered hybernation mode '.center(50, '='))
			break