import os
from src.mlproject import logger
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    reads yaml file and returns

    Args:
        path_to_yaml (Path): path to yaml file
    Raises:
        ValueError: if yaml file is empty
        FileNotFoundError: if yaml file is not found
        e : empty file
    Returns:
        ConfigBox: ConfigBox object containing the yaml file content
        
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e 


@ensure_annotations
def create_directories(path_to_directories: list , verbose=True):
    """"
    create list of directories
    Args:
        path_to_directories (list): list of directories to be created
        verbose (bool): if True, print the directory created
    
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose :
            logger.info(f"created directory at : {path}")

@ensure_annotations
def save_json(path: Path , data:dict):
    """
    Save data to json file
    Args:
        path (Path): path to  json file
    Returns:
        CofigBox :  data as class attribute instead of dict
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"json file loaded successfully from  : {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any, path: Path):
    """
    Save data to binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"data saved successfully at : {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load data from binary file
    Args:
        path (Path): path to binary file
    Returns:
        Any : data loaded from binary file
    """
    data = joblib.load(path)
    logger.info(f"data loaded successfully from : {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file or directory
    Args:
        path (Path): path to file or directory
    Returns:
        str : size of file or directory
    """
    
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"{size_in_kb} KB"