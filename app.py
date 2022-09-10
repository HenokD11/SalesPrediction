import os
import sys
import streamlit as st

sys.path.insert(0, './scripts')


st.set_page_config(page_title="Rossmann Sales Predictions", layout="wide")

from multiapp import MultiApp
from appl import viz, model

app = MultiApp()

st.sidebar.markdown("""
# Rossmann Sales Predictions
""")

with open('./scripts/web-css/styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Add all your application here
app.add_app("visualizations", viz.app)
app.add_app("model-prediction", model.app)

# The main app
app.run()