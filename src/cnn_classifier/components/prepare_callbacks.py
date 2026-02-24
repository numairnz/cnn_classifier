import time
import os

import tensorflow as tf
from cnn_classifier.entity.config_entity import PrepareCallbacksConfig
class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config
    @property
    def create_tb_callbacks(self):
        time_stamp =time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log_dir,f"tb_logs_at{time_stamp}")
        return tf.keras.callbacks.TensorBoard(log_dir = tb_running_log_dir)
    @property
    def create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(filepath=self.config.checkpoint_model_filepath, save_best_only=True)
    
    def get_tb_ckpt_callbacks(self):
        return ([self.create_tb_callbacks,self.create_ckpt_callbacks])
