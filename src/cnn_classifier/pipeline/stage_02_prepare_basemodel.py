import os
from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.components.preparebasemodel import PrepareBaseModel
from cnn_classifier import logger
class PrepareModel:
    def __init__(self):
        pass
    def main(self):
        STAGE_NAME = 'Base Model'
        logger.info(f'Preparing {STAGE_NAME} Started')
        try:
            config= ConfigurationManager()
            config = config.get_base_model_config()
            base_model = PrepareBaseModel(config)
            base_model.get_base_model()
            base_model.update_base_model()
        except Exception as e:
            logger.exception(e)
            raise e


if __name__ == '__main__':
    try:
        prepare_model = PrepareModel()
        prepare_model.main()
    except Exception as e:
        logger.exception(e)
        raise e