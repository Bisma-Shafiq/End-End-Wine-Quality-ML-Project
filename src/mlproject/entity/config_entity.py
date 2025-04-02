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