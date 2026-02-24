import os
import urllib.request as request
import zipfile
from cnn_classifier.utils.common import get_size
from cnn_classifier import logger
from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.entity.config_entity import DataIngestionConfig
from pathlib import Path
class DataIngestion:
    def __init__(self,config: DataIngestionConfig):
        self.config = config
    def download_files(self):
        if not os.path.exists(self.config.local_data_files):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_files
            )
            logger.info(f"{filename} downloaded with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_files))}")
        
    def extract_unzip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

