import yaml
import os
from datetime import date as dt

class Config:

    def __init__(self, path_to_config = 'config.yaml'):
        """
            Description:
                Loads parameters from config.yaml into global object
            
            Arguments:
                path_to_config (str): path where config.yaml file is stored

            Attributes:
                rundate (int): see arguments
        """

        self.path_to_config = path_to_config
        
        if os.path.isfile(self.path_to_config):
            pass
        else:
            self.path_to_config = path_to_config

        with open(self.path_to_config, 'r') as f:
            self.dictionary = yaml.load(f.read(), Loader=yaml.FullLoader)

        for k, v in self.dictionary.items():
            setattr(self, k, v)