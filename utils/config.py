import yaml
import os
import sys

with open("config.yaml", "r") as file:
    config:dict = yaml.safe_load(file)

config['database']['chromadb']['name'] = 'chromadb.db' if not config['database']['chromadb']['name'] \
    else config['database']['chromadb']['name']

if not config.get('data_path'):
    if sys.platform.startswith('linux'):
        # create dir
        if not os.path.exists('/app/data'):
            os.makedirs('/app/data')
        config['data_path'] = '/app/data'
    else:
        config['data_path'] = os.path.join('.')

