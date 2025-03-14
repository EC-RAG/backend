import yaml

with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)

config['database']['chromadb']['name'] = 'chromadb.db' if not config['database']['chromadb']['name'] \
    else config['database']['chromadb']['name']

