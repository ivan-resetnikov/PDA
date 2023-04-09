import configparser



config = configparser.ConfigParser()
config.read('config.cfg')


name = config['settings']['name']
voiceSex = config['voice']['voic_sex']