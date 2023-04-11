import core

core.speech.setVoice(core.const.sex)



def sleepLoop () :
	while True :
		command = core.speech.recognize()

		if core.speech.ratio(command, f'open {core.const.name}') > 50 or \
		   core.speech.ratio(command, f'hey {core.const.name}') > 50 or \
		   core.speech.ratio(command, f'{core.const.name}') > 50 :
			core.loop.wakeLoop()

		elif core.speech.ratio(command, 'shutdown') > 60:
			core.speech.say('Shutdown requested. Initiated protocol. Shutting down')
			break


if __name__ == '__main__':
	try: sleepLoop()
	except KeyboardInterrupt: print(' Done '.center(50, '='))