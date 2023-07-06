import yaml
import os

def yaml_reader(option):
    root_dir = os.path.dirname(os.path.abspath(__file__)) 
    parent_dir = os.path.dirname(root_dir)

    with open(f"{parent_dir}/config.yaml" , 'r') as file:
        data = yaml.safe_load(file)
        
    if option in data:
        return data[option]
    elif option == "root_data":
        data_dir = f"{parent_dir}/data"
        return data_dir
    else:
        raise ValueError(f"Option {option} is not found in the YAML file.")
