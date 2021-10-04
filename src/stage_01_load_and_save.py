from src.utils.all_utils import create_dir, read_yaml
import os
import argparse
import pandas as pd

#get data from the config.yaml
def get_data(config_path):
    yaml_contents = read_yaml(config_path)
    print(yaml_contents)
    df = pd.read_csv(yaml_contents['input_data'], sep=";")
    print(df.head())
    #save the data local directory
    artifacts_dir = yaml_contents['artifacts']['artifacts_dir']
    raw_local_dir = yaml_contents['artifacts']['raw_local_dir']
    raw_local_file = yaml_contents['artifacts']['raw_local_file']

    print(artifacts_dir, raw_local_dir, raw_local_file)

    raw_local_dir_path = os.path.join(artifacts_dir, raw_local_dir)
    
    create_dir([raw_local_dir_path])

    raw_local_file_path = os.path.join(raw_local_dir_path, raw_local_file)
    print(raw_local_file_path)

    df.to_csv(raw_local_file_path, sep=',', index=False)


if __name__ == '__main__':

    # Reading the config yaml as the command line args to get the data as per the data source in the config.yaml file
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default = "config/config.yaml")
    parsed_args = args.parse_args()
    get_data(parsed_args.config)



