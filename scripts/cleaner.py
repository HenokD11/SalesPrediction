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

    def separate_date_column(self, date_column: str, drop_date=True) -> pd.DataFrame:
        try:
            date_index = self.df.columns.get_loc(date_column)
            self.df.insert(date_index + 1, 'Year', self.df[date_column].apply(
                lambda x: x.date().year))
            self.df.insert(date_index + 2, 'Month', self.df[date_column].apply(
                lambda x: x.date().month))
            self.df.insert(date_index + 3, 'Day',
                           self.df[date_column].apply(lambda x: x.date().day))

            if(drop_date):
                self.df = self.df.drop(date_column, axis=1)
        except:
            print("Failed to separate the date to its components")

    def change_column_to_date_type(self, col_name: str) -> None:
        try:
            self.df[col_name] = pd.to_datetime(self.df[col_name])
        except:
            print('failed to change column to Date Type')
        self.logger.info(
            f"Successfully changed column {col_name} to Date Type")

    def remove_nulls(self) -> pd.DataFrame:
        return self.df.dropna()

    def add_season_col(self, month_col: str) -> None:
        # helper function
        def get_season(month: int):
            if(month <= 2 or month == 12):
                return 'Winter'
            elif(month > 2 and month <= 5):
                return 'Spring'
            elif(month > 5 and month <= 8):
                return 'Summer'
            else:
                return 'Autumn'

        try:
            month_index = self.df.columns.get_loc(month_col)
            self.df.insert(month_index + 1, 'Season',
                           self.df[month_col].apply(get_season))

        except:
            print("Failed to add season column")
        self.logger.info(f"Successfully added season column to {month_col}")

    def change_columns_type_to(self, cols: list, data_type: str) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns data types are changed to the specified data type
        Parameters
        ----------
        cols:
            Type: list
        data_type:
            Type: str
        Returns
        -------
        pd.DataFrame
        """
        try:
            for col in cols:
                self.df[col] = self.df[col].astype(data_type)
        except:
            print('Failed to change columns type')
        self.logger.info(f"Successfully changed columns type to {data_type}")
        return self.df