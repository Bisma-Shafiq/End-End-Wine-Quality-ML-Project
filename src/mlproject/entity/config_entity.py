#create entity
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any
from pathlib import Path

#data ingestion config
@dataclass(frozen=True) # frozen=True makes the dataclass immutable
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:Path


#data validation config
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict

# data transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path

# model trainer
@dataclass(frozen=True)
class ModelTrainningConfig:
    root_dir: Path
    train_data_path: Path  
    test_data_path: Path   
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str

#model evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path   
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
  