import core

core.speech.setVoice(core.const.voice)



def sleepLoop () :
	while True :
		command = core.speech.recognize()

		if core.speech.ratio(command, f'open {core.const.name}') > 60 or \
		   core.speech.ratio(command, f'hey {core.const.name}')  > 60 :
			core.loop.wakeLoop()

		elif core.speech.ratio(command, 'shutdown') > 60:
			core.speech.say('Shutdown protocol, initiated. shutting down')
			break


if __name__ == '__main__':
	try: sleepLoop()
	except KeyboardInterrupt: print('Done')