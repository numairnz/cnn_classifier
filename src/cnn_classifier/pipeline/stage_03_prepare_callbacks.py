from cnn_classifier.config.configuration import ConfigurationManager
from cnn_classifier.components import prepare_callbacks
from cnn_classifier import logger

class PrepareCallbacks:
    def __init__(self):
        pass
    def main(self):
        STAGE_NAME = 'Prepare_Callbacks'
        logger.info(f"{'>>'*20} {STAGE_NAME} {'<<'*20}")
        try:
            logger.info(f"{'>>'*20} {STAGE_NAME} Started {'<<'*20}")
            config = ConfigurationManager()
            prepare_callbacks_config = config.get_prepare_callbacks_config()
            prepare_callbacks = PrepareCallbacks(config = prepare_callbacks_config)
            prepare_callbacks.get_tb_ckpt_callbacks()
            logger.info(f"{'>>'*20} {STAGE_NAME} Completed {'<<'*20}")
        except Exception as e:
            raise e
    
    if __name__ == '__main__':
        try:
            prepare_callbacks = PrepareCallbacks()
            prepare_callbacks.main()
        except Exception as e:
            raise e
