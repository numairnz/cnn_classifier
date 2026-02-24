from cnn_classifier import logger
from cnn_classifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnn_classifier.pipeline.stage_02_prepare_basemodel import PrepareModel
STAGE_NAME = 'Data Ingestion Stage'
logger.info(f"{'>>'*20}{STAGE_NAME} {'<<'*20}")


try:
    logger.info(f"{'>>'*20}{STAGE_NAME} Started {'<<'*20}")
    data_ingestion = DataIngestionTrainingPipeline() 
    data_ingestion.main()
    logger.info(f"{'>>'*20}{STAGE_NAME} Completed {'<<'*20}\n\n x=================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model Stage'
logger.info(f"{'>>'*20}{STAGE_NAME} {'<<'*20}")
try:
    logger.info(f"{'>>'*20}{STAGE_NAME} Started {'<<'*20}")
    prepare_base_model = PrepareModel()
    prepare_base_model.main()
    logger.info(f"{'>>'*20}{STAGE_NAME} Completed {'<<'*20}\n\n x=================x")
except Exception as e:
    logger.exception(e)
    raise e

