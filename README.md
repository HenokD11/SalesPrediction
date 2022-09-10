# Rossmann Pharmaceutical Sales Prediction

# About

The finance team at Rossman Pharmaceuticals wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgment to forecast sales.

The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.

The task was to build and serve an end-to-end product that delivers this prediction to analysts in the finance team.

# Scenario

You work at Rossmann Pharmaceuticals as a Machine Learning Engineer. The finance team wants to forecast sales in all their stores across several cities six weeks ahead of time. Managers in individual stores rely on their years of experience as well as their personal judgement to forecast sales.

The data team identified factors such as promotions, competition, school and state holidays, seasonality, and locality as necessary for predicting the sales across the various stores.

Your job is to build and serve an end-to-end product that delivers this prediction to analysts in the finance team.

# Approach

- The project is divided and implemented by the following phases

    - Exploration of customer purchasing behavior
    - Prediction of store sales
        - Machine learning approach
        - Deep Learning approach
    - Serving predictions on a web interface

# Project Structure

The repository has a number of files including python scripts, jupyter notebooks and text files. Here is their structure with a brief explanation.

**data:**

    the folder where the dataset csv files are stored

**.github:**

    the folder where github actions and CML workflow is integrated

**.dvc:**

    the folder where dvc is managed and configured for remote data version control

**models:**

    the folder where model pickle files and model reference csv files are stored

**notebooks:**

*EDA.ipynb:* a jupyter notebook for exploring the data
*ML_DataPrep.ipynb:* a jupyter notebook for preprocessing the data for ML and further analysis
*preprocessing:* cleaning pandas dataframes
*lstm.ipynb:* a jupyter notebook training an LSTM model for forecasting purpose
*train_regression.ipynb:* a jupyter notebook training an Regression models for prediction purpose

**scripts**

*ML_modelling_utils.py:* a python script for handle model name creation and manipulation
*cleaner.py:* a python script for cleaning pandas dataframes
*data_preprocessing.py:* a python script for cleaning pandas dataframes
*data_manipulation.py:* a python script for manipulating dataframes
*multiapp.py:* a python script for creating a multipaged streamlit app
*log_helper.py:* a python script that creates python based logger and helps user log different messages

**tests:**

    the folder containing unit tests for components in the scripts

**root folder:**

*requirements.txt:* a text file lsiting the projet's dependancies
*app.py:* entry file for the streamlit application
*setup.py:* a configuration file for installing the scripts as a package
*README.md:* Markdown text with a brief explanation of the project and the repository structure.

