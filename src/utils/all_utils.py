#utility file that have all the common functions defined for reuse

import yaml
import os

def read_yaml(yaml_file):
    with open(yaml_file, 'r') as fp:
        content = yaml.safe_load(fp)
    return content

def create_dir(dir_list):
    for dir in dir_list:
        os.makedirs(dir, exist_ok=True)
        print(f"created directory {dir}")
    return None

        




