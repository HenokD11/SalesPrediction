import pandas as pd
import numpy as np
from log_helper import App_Logger

app_logger = App_Logger("../logs/data_cleaner.log").get_app_logger()


class DataCleaner:
    def __init__(self, df: pd.DataFrame, deep=False) -> None:
        """
        Returns a DataCleaner Object with the passed DataFrame Data set as its own DataFrame
        Parameters
        ----------
        df:
            Type: pd.DataFrame
        Returns
        -------
        None
        """
        self.logger = App_Logger(
            "../logs/data_cleaner.log").get_app_logger()
        if(deep):
            self.df = df.copy(deep=True)
        else:
            self.df = df

    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        Parameters
        ----------
        columns:
            Type: list
        Returns
        -------
        pd.DataFrame
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def separate_date_time_column(self, column: str, col_prefix_name: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns is split to date and time new columns adding a prefix string to both
        Parameters
        ----------
        column:
            Type: str
        col_prefix_name:
            Type: str
        Returns
        -------
        pd.DataFrame
        """
        try:

            self.df[f'{col_prefix_name}Date'] = pd.to_datetime(
                self.df[column]).dt.date
            self.df[f'{col_prefix_name}Time'] = pd.to_datetime(
                self.df[column]).dt.time

            return self.df

        except:
            print("Failed to separate the date-time column")
