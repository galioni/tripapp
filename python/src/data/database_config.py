import os
import configparser

class DBConfig:
    
    #Get database configurations
    def get_db(self):
      config = configparser.ConfigParser()
      config.read(os.path.abspath('config.ini'))
      databaseType = config['Global']['DatabaseType']

      if databaseType == 'MongoDB':
        self.host = config['MongoDB']['Host']
        self.database = config['MongoDB']['Database']
        
