import json
import yaml
import csv
from pprint import pprint


FILENAME_JSON = 'input.json'
FILENAME_CSV = 'input.csv'
FILENAME_YAML = 'input.yaml'

def json_loader(filepath):
    with open(FILENAME_JSON, 'r') as json_file:
        json_data = json.load(json_file)

def yaml_loader(filepath):
    with open(FILENAME_YAML, 'r') as yaml_file:
        yaml_data = yaml.load(yaml_file)

def csv_loader(filepath):
    with open(FILENAME_CSV, 'r') as csv_file:
        reader = csv.reader(FILENAME_CSV)
        names = next(reader)
        lines = [l for l in reader]

if __name__ == "__main__":
    yaml_file = "input.yaml"
    yaml_data = yaml.load(yaml_file)
    return (yaml_data)









