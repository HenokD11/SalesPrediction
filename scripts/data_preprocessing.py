
import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')
sys.path.append(os.path.abspath(os.path.join('..')))

from log_helper import App_Logger

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

    def convert_to_numbers(self) -> pd.DataFrame:
        self.df = self.df.apply(pd.to_numeric, errors='coerce')
        self.logger.info(f"Converted to numbers")
        return self.df

    def convertByteMB(self, coll) -> pd.DataFrame:
        for col in coll:
            self.df[col] = self.df[col] / 1*10e+5
            self.df.rename(
                columns={col: f'{col[:-7]}(MegaBytes)'}, inplace=True)
        print('Byte to MB change error')
        return self.df

    def show_datatypes(self) -> pd.DataFrame:
        self.logger.info(f"Showing datatypes")
        return self.df.dtypes

    def show_data_description(self) -> pd.DataFrame:
        self.logger.info(f"Showing data description")
        return self.df.describe()

    def show_data_information(self) -> pd.DataFrame:
        self.logger.info(f"Showing data information")
        return self.df.info()

    def show_statistical_info(self) -> pd.DataFrame:
        self.logger.info(f"Showing statistical info")
        return self.df.agg(['mean'])

    def show_correlation(self) -> pd.DataFrame:
        self.logger.info(f"Showing correlation")
        return self.df.corr()

    
    