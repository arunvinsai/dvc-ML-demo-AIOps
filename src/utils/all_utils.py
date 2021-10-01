import yaml
import os

def read_yaml(yaml_file):
    with open(yaml_file, 'r') as fp:
        content = yaml.safe_load(fp)
    return content
