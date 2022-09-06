
import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')
sys.path.append(os.path.abspath(os.path.join('..')))

from log_help import App_Logger

app_logger = App_Logger("logs/data_preProcessing.log").get_app_logger()


class data_preProcessing_script:

    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.logger = App_Logger(
            "logs/data_preProcessing.log").get_app_logger()

    def drop_duplicates(self) -> pd.DataFrame:
        droped = self.df[self.df.duplicated()].index
        self.logger.info(f"Dropped duplicates: {droped}")
        return self.df.drop(index=droped, inplace=True)