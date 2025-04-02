import os
from sklearn.model_selection import train_test_split
import pandas as pd
from src.mlproject import logger
from sklearn.linear_model import ElasticNet
import joblib
from src.mlproject.entity.config_entity import ModelTrainningConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainningConfig):
        self.config = config
    
    def train(self):
        # Fix: Use train_data_path instead of train_data_dir
        train_data = pd.read_csv(self.config.train_data_path)
        # Fix: Use test_data_path instead of test_data_dir
        test_data = pd.read_csv(self.config.test_data_path)
        
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[self.config.target_column]
        test_y = test_data[self.config.target_column]
        
        regression_model = ElasticNet(
            alpha=self.config.alpha,
            l1_ratio=self.config.l1_ratio,
            random_state=42
        )
        
        regression_model.fit(train_x, train_y)
        
        joblib.dump(
            regression_model, 
            os.path.join(self.config.root_dir, self.config.model_name)
        )