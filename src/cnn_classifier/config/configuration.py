from cnn_classifier.constants import *
from cnn_classifier.utils.common import read_yaml,create_directories
from cnn_classifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig, PrepareCallbacksConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_files=config.local_data_files,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    
    def get_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        params= self.params
        create_directories([config.root_dir])
        PrepareBaseModel = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path = config.base_model_path,
            updated_base_model_path = config.updated_base_model_path,
            params_image_size = params.IMAGE_SIZE,
            params_learning_rate = params.LEARNING_RATE,
            params_include_top = params.INCLUDE_TOP,
            params_weights = params.WEIGHTS,
            params_classes = params.CLASSES
        )
        return PrepareBaseModel
    def get_prepare_callbacks_config(self) -> PrepareCallbacksConfig:
        config=self.config
        create_directories([Path(config.prepare_callbacks.root_dir)])
        checkpoint_dir = os.path.dirname(config.prepare_callbacks.checkpoint_model_filepath)
        create_directories([Path(config.prepare_callbacks.tensorboard_root_log_dir),Path(checkpoint_dir)])
        prepare_callbacks_config = PrepareCallbacksConfig(
            root_dir = Path(config.prepare_callbacks.root_dir),
            tensorboard_root_log_dir = Path(config.prepare_callbacks.tensorboard_root_log_dir),
            checkpoint_model_filepath = Path(config.prepare_callbacks.checkpoint_model_filepath)
        )
        return prepare_callbacks_config
   

