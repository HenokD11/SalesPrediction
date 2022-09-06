import pandas as pd
from sklearn.preprocessing import MinMaxScaler, Normalizer, StandardScaler, LabelEncoder
from datetime import datetime
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
sys.path.insert(0, '../scripts/')
sys.path.insert(0, '../logs/')

from log_helper import App_Logger

app_logger = App_Logger("../logs/data_manipulator.log").get_app_logger()

class DataManipulator:
    def __init__(self, df: pd.DataFrame, deep=False):
        """
            Returns a DataManipulator Object with the passed DataFrame Data set as its own DataFrame
            Parameters
            ----------
            df:
                Type: pd.DataFrame
            Returns
            -------
            None
        """
        self.logger = App_Logger(
            "../logs/data_manipulator.log").get_app_logger()
        if(deep):
            self.df = df.copy(deep=True)
        else:
            self.df = df

    def add_week_day(self, day_of_week_col: str) -> pd.DataFrame:
        try:
            date_index = self.df.columns.get_loc(day_of_week_col)
            self.df.insert(date_index + 1, 'WeekDay',
                           self.df[day_of_week_col].apply(lambda x: 1 if x <= 5 else 0))

            self.logger.info("Successfully Added WeekDay Column to the DataFrame")

        except Exception as e:
            self.logger.exception("Failed to Add WeekDay Column")

    def add_week_ends(self, day_of_week_col: str) -> pd.DataFrame:
        try:
            date_index = self.df.columns.get_loc(day_of_week_col)
            self.df.insert(date_index + 1, 'WeekEnd',
                           self.df[day_of_week_col].apply(lambda x: 1 if x > 5 else 0))

            self.logger.info("Successfully Added WeekEnd Column to the DataFrame")

        except Exception as e:
            self.logger.exception("Failed to Add WeekEnd Column")

    # Considering christmas lasts for 12 days, Easter for 50 days and public holidays for 1 day.
    # And considering before and after periods to be 5 less and 5 more days before and after the holiday for christmas
    # and 10 days for Easter
    # And 3 days for public holiday
    # get state holiday list
    # a = public holiday, b = Easter holiday, c = Christmas, 0 = None

    def affect_list(self, change_list, interval, duration, index):
        start_pt = int(index-duration/2) - interval
        try:
            for index in range(start_pt, start_pt + interval):
                change_list[index] = 'before'
            for index in range(start_pt + interval, start_pt + interval + duration):
                change_list[index] = 'during'
            for index in range(start_pt + interval + duration, start_pt + interval + duration + interval):
                change_list[index] = 'after'
        except:
            pass

        return change_list

    def modify_holiday_list(self, holiday_list: list) -> list:
        new_index = ["neither"] * len(holiday_list)
        for index, value in enumerate(holiday_list):
            if value == 'a':  # public holiday
                self.affect_list(new_index, 3, 1, index)
            elif value == 'b':  # Easter
                self.affect_list(new_index, 10, 50, index)
            elif value == 'c':  # christmas
                self.affect_list(new_index, 5, 12, index)
            else:
                pass

        return new_index
