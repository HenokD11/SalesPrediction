import streamlit as st
import pandas as pd
import sys
import pickle


def app():

    st.title("Rosmann Pharmaceutical Sales Prediction")

    st.header("Distribution and Visualization of the pharmaceutical Data")

    st.subheader("Correlation Analysis")
    st.image('img/dashboard/correlation_analysis.png')

    st.subheader("Open Stores On Week Days")
    st.image('img/dashboard/openStores_onWeekDays.png')

    st.subheader("Customer Behaviour On Store Open and Close Time")
    st.image('img/dashboard/customer_behaviour_onStoreOpenCloseTime.png')

    st.subheader("Assortment Effect On Sales")
    st.image('img/dashboard/assortment_effect.png')

    st.subheader("Competitor Distance Effect On Sales")
    st.image('img/dashboard/compettor_distance_effect.png')

    st.subheader("Promotion Distribution On Train and Test Data")
    st.image('img/dashboard/promotion_distribution_OntrainData.png')

    st.subheader("Open Stores on WeekDays")
    st.image('img/dashboard/openStores_onWeekDays.png')

    st.subheader("promotion and month relation")
    st.image('img/dashboard/promo_month_relation.png')

    st.subheader("promotion and customer relation")
    st.image('img/dashboard/promotion_customer_relation.png')

    st.subheader("promotion distribution On trainData")
    st.image('img/dashboard/promotion_distribution_OntrainData.png')

    st.subheader("promotion and sales relation")
    st.image('img/dashboard/promotion_sales_relation.png')

    st.subheader("sales and cusotmer relation on DaysOfWeek")
    st.image('img/dashboard/sales_cusotmer_onDaysOfWeek.png')

    st.subheader("sales and customer on Holidays")
    st.image('img/dashboard/sales_customer_onHoliday.png')

    st.subheader("sales and customer relation on Specific Holidays")
    st.image('img/dashboard/sales_customer_onSpecificHolidays.png')

    st.subheader("sales and customers relations on Store Type")
    st.image('img/dashboard/sales_customers_onStoreType.png')

    st.subheader("sales on weekDays")
    st.image('img/dashboard/sales_onweekDays.png')

    st.subheader("storeType open Count within WeekDays")
    st.image('img/dashboard/storeType_openCountwithInWeekDays.png')

    st.header("Model Analysis")

    st.subheader("test and val loss plot")
    st.image('img/dashboard/test_val_plot.png')

    st.subheader("Feature Importance on model")
    st.image('img/dashboard/featureImportanceOfAmodel.png')

    st.subheader("Prediciton image - Time Series")
    st.image('img/dashboard/Prediciton image.png')