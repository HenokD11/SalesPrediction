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

    def remove_single_value_columns(self, unique_value_counts: pd.DataFrame) -> pd.DataFrame:
        """
        Returns a DataFrame where columns with a single value are removed
        Parameters
        ----------
        unique_value_counts:
            Type: pd.DataFrame
        Returns
        -------
        pd.DataFrame
        """
        drop_cols = list(
            unique_value_counts.loc[unique_value_counts['Unique Value Count'] == 1].index)
        return self.df.drop(drop_cols, axis=1, inplace=True)

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Returns a DataFrame where duplicate rows are removed
        Parameters
        ----------
        None
        Returns
        -------
        pd.DataFrame
        """
        removables = self.df[self.df.duplicated()].index
        return self.df.drop(index=removables, inplace=True)

    def fill_numeric_values(self, missing_cols: list, acceptable_skewness: float = 5.0) -> pd.DataFrame:
        """
        Returns a DataFrame where numeric columns are filled with either median or mean based on their skewness
        Parameters
        ----------
        missing_cols:
            Type: list
        acceptable_skewness:
            Type: float
            Default value = 5.0
        Returns
        -------
        pd.DataFrame
        """
        df_skew_data = self.df[missing_cols]
        df_skew = df_skew_data.skew(axis=0, skipna=True)
        for i in df_skew.index:
            if(df_skew[i] < acceptable_skewness and df_skew[i] > (acceptable_skewness * -1)):
                value = self.df[i].mean()
                self.df[i].fillna(value, inplace=True)
            else:
                value = self.df[i].median()
                self.df[i].fillna(value, inplace=True)

        return self.df

    def add_columns_from_another_df_using_column(self, from_df: pd.DataFrame, base_col: str, add_columns: list) -> pd.DataFrame:
        try:
            new_df = self.df.copy(deep=True)
            from_df.sort_values(base_col, ascending=True, inplace=True)
            for col in add_columns:
                col_index = from_df.columns.tolist().index(col)
                new_df[col] = new_df[base_col].apply(
                    lambda x: from_df.iloc[x-1, col_index])

            return new_df

        except:
            print('Failed to add columns from other dataframe')