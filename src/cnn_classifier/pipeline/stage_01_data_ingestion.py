
from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.components.data_ingestion import DataIngestion
from cnn_classifier import  logger

STAGE_NAME = 'Data Ingestion Stage'


class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        logger.info(f"{'>>'*20}{STAGE_NAME} {'<<'*20}")
        config =  ConfigurationManager()
        data_ingestion_config = DataIngestion(config.get_data_ingestion_config())
        data_ingestion_config.download_files()
        data_ingestion_config.extract_unzip_file()
if __name__ == '__main__':
    try:
        data_ingestion_training_pipeline = DataIngestionTrainingPipeline()
        data_ingestion_training_pipeline.main()
    except Exception as e:
        raise e




        