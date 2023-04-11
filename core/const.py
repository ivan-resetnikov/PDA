import configparser



config = configparser.ConfigParser()
config.read('config.cfg')


name = config['settings']['name']
sex  = config['voice']['sex']