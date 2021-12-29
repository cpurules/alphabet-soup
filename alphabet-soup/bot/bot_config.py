import json
import os

class BotConfig:
    def __init__(self, config_file):
        if config_file is None or config_file == '':
            raise ValueError('Missing config_file argument')
        
        if not os.path.exists(config_file):
            raise FileNotFoundError('Could not find configuration file {0}'.format(config_file))
        
        with open(config_file, 'r') as f:
            try:
                config_dict = json.load(f)
            except Exception as e:
                raise Exception('Error while parsing config file {0}: {1}'.format(config_file, e))
        
        try:
            try:
                self.OWNER_ID = int(config_dict['OWNER_ID'])
                if self.OWNER_ID == 0:
                    raise ValueError('No value specified for OWNER_ID')
            except ValueError as e:
                raise ValueError('Error while parsing OWNER_ID: {0}'.format(str(e)))
            
            self.BOT_TOKEN = os.getenv('BOT_TOKEN')
            if self.BOT_TOKEN is None or self.BOT_TOKEN == '':
                raise ValueError('Missing BOT_TOKEN environment variable')
        except KeyError as e:
            raise KeyError('{0} is missing from the configuration file'.format(str(e)))