import core

from datetime import datetime
from os       import system



name = ''

core.speech.setVoice('female')


def mainLoop () :
	while True :
		core.speech.say('I\'m listening')

		command = core.speech.recognize()


		if core.speech.tokenRatio('access database', command) > 60 :
			if 'remote' in command :
				pleased = False
				while not pleased :
					core.speech.say('Say remote database entry')
					pleased = core.database.accessRemoteDatabase(core.speech.recognize())

			elif 'local' in command :
				pleased = core.database.accessLocalDatabase()


		elif core.speech.ratio(command, 'create database and three') > 40 : core.database.createDatabaseEntry()


		elif core.speech.ratio(command, 'open youtube') > 60 : system('start https://youtube.com/')


		elif core.speech.tokenRatio(command, 'what is it') > 55 :
			if 'time' in command :
				time = datetime.now()
				core.speech.say('{}:{}'.format(str(time.hour).rjust(2, 'O'), str(time.minute).rjust(2, 'O')))

			elif 'date' in command :
				time = datetime.now()
				core.speech.say(time.strftime("%B %d, %Y"))


		elif core.speech.ratio(command, 'open games list') > 60 : system('start D:/Main/Games')


		elif core.speech.ratio(command, 'thanks') > 60 : core.speech.say('You are welcome :)')


		elif core.speech.ratio(command, 'stop') > 60 or core.speech.ratio(command, 'that\'s all') > 60 or core.speech.ratio(command, 'that is it') > 60 or core.speech.ratio(command, 'enter hybernation mode') > 60 or core.speech.ratio(command, 'start hybernation') > 60 or core.speech.ratio(command, 'sleep') > 60 :
			core.speech.say(f'Entering hybernation mode, say "open {name}" again, to start interaction')
			break


def wakeLoop () :
	while True :
		command = core.speech.recognize()

		if core.speech.ratio(command, f'open {name}') > 60 or core.speech.ratio(command, f'hey {name}') > 60 : # akses remout detabejs
			mainLoop()

		elif core.speech.ratio(command, 'initialize shutdown protocol') > 60 :
			core.speech.say('Shutdown protocol, initiated. shutting down')
			break


if __name__ == '__main__' :
	try : wakeLoop()
	except KeyboardInterrupt : print('Done')