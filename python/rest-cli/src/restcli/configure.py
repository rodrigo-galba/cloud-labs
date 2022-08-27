import os
import configparser
import pathlib

HOME_DIR='~/.restcli'

def init(data):
    
    config = configparser.ConfigParser()
    config['default'] = data

    pathlib.Path(os.path.expanduser(HOME_DIR)).mkdir(parents=True, exist_ok=True)

    with open(os.path.join(os.path.expanduser(HOME_DIR), 'config'), 'w') as configFile:
        config.write(configFile)

    print('Configurations saved: ', os.path.join(os.path.expanduser(HOME_DIR), 'config'))
