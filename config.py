## functions for changing configuration settings.
## config settings are stored in config.json.

import json

def set_transloc_key(key):
    # changes api key in the config file.
    # input: key - string api_key from transloc api.
    try:
        config_file = open('config.json', 'r')
        config_data = json.load(config_file) 
        config_file.close() 

    except FileNotFoundError:
        config_data = {} 
        
    config_data['api_key'] = key
    config_file = open('config.json', 'w') 
    json.dump(config_data, config_file) 
    config_file.close() 


def get_transloc_key():
    # gets api_key from config.json.
    try:
        config_file = open('config.json', 'r') 
        key = json.load(config_file)['api_key'] 
        config_file.close() 
        return key 
    except FileNotFoundError:
        raise Exception("Need to set your api key first.")
    except KeyError:
        raise Exception("config error - need to set api key.")