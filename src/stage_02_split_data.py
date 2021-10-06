from src.utils.all_utils import create_dir, read_yaml, save_data
import os
import argparse
import pandas as pd
from sklearn.model_selection import train_test_split

#get data from the config.yaml
def split_data(config_path, params_path):
    yaml_contents = read_yaml(config_path)
    params = read_yaml(params_path)
    #print(yaml_contents)
    print(params)
    
    artifacts_dir = yaml_contents['artifacts']['artifacts_dir']
    raw_local_dir = yaml_contents['artifacts']['raw_local_dir']
    raw_local_file = yaml_contents['artifacts']['raw_local_file']

    #print(artifacts_dir, raw_local_dir, raw_local_file)

    raw_local_file_path = os.path.join(artifacts_dir, raw_local_dir, raw_local_file)
    #print(raw_local_file_path)

    df = pd.read_csv(raw_local_file_path)
    print(df.head())
    print(params['base']['test_size'])
    split_ratio = params['base']['test_size']
    random_state = params['base']['random_state']

    print(split_data, type(split_data))

    train, test = train_test_split(df, test_size=split_ratio, random_state=random_state)

    split_data_dir = yaml_contents['artifacts']['split_data_dir']
    split_data_dirname = os.path.join(artifacts_dir, split_data_dir)
    create_dir([split_data_dirname])

    train_data_filename = yaml_contents['artifacts']['train']
    test_data_filename = yaml_contents['artifacts']['test']

    train_data_path = os.path.join(split_data_dirname, train_data_filename)
    test_data_path = os.path.join(split_data_dirname, test_data_filename)

    save_data(train, train_data_path)
    save_data(test, test_data_path)


if __name__ == '__main__':

    # Reading the config yaml as the command line args to get the data as per the data source in the config.yaml file
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default = "config/config.yaml")
    args.add_argument("--params", "-p", default = "params.yaml")
    parsed_args = args.parse_args()
    split_data(config_path = parsed_args.config, params_path = parsed_args.params)



