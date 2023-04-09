from .speech import say, setRate, setRate, ratio, recognize

from threading import Thread
from os        import listdir, system

import wikipedia


def createDatabaseEntry () :
	say('Say the name, describe the topic in 2 sentences. Started recording.')

	data = ''

	while True :
		data += recognize(False) + ' '

		say('Finish entry?')
		if ratio('yes', recognize()) > 60 or ratio('yeah', recognize()) > 60 :
			say('Name current entry: ')
			name = recognize()

			filename = name
			filename.replace(' ', '_')
			filename.replace('.', '_')

			say('Outputing results to database.')
			with open(f'./database/{filename}.txt', 'w') as file :
				file.write(f'[{name}]\n\n{data}')
		
			say('Would you like to start manual editor: ')
			if ratio('yes', recognize()) > 60 or ratio('yeah', recognize()) > 60 :
				say('Opening editor...')
				system(f'start ./database/{filename}.txt')

			else :
				say('Ok')
				break

		else :
			say('Keep talking')


def accessLocalDatabase () :
	topics = ''

	for i, topic in enumerate(listdir('./database/')) :
		topic = topic[:-4:]
		topics += f'{i} - {topic};\n'

	say(f'Listing full list of entries in local database: \n{topics}')

	say('Which one would you like to edit?')
	name = recognize()

	name.replace(' ', '_')
	name.replace('.', '_')

	for file in listdir('./database/') :
		if ratio(name, file) > 40 :
			filename = file
			break

	with open(f'./database/{filename}', 'r') as file :
		lines = file.readlines()

		name = lines[0][1:-1:]

		data = '\n'.join(lines[2::])

	say(f'{name}... {data}')


def accessRemoteDatabase (topic:str, sentences:int=2) :
	try :
		try :
			setRate(170)
			say(wikipedia.summary(topic, sentences=sentences))
			setRate(200)

			pleased = True

		except wikipedia.exceptions.DisambiguationError :
			pleased = False

			Thread(target=say, args=(f'Topic {topic} not found, searching similar keywords',)).start()

			alternatives = wikipedia.search(topic)

			say('Found, {} results. '.format(len(alternatives)))
			say(', '.join(alternatives)[:-2:])

		except wikipedia.exceptions.PageError :
			say('Couldn find any info about the topic, whould you like to add it yourself?')

			if ratio('yes', recognize()) > 60 or ratio('yeah', recognize()) > 60 : createDatabaseEntry()

			else : say('Ok')

			pleased = True

		return pleased

	except :
		say('Error ocured while attempting accessing remote database')
		return False