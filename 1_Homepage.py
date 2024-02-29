import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
import yaml #PyYAML
from yaml.loader import SafeLoader

from packages import utils


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(
    page_title='Multipage App',
    page_icon='👋',
    layout="wide"
)

def homepage(username):
    # st.sidebar.write(f'*Welcome, {username}*')
    # st.title('My Dashboard')
    df1, df2 = utils.load_datasets()
    st.markdown(f"""
                Welcome to the World Countries Data Analysis Dashboard! 
                This website aims at showing interesting statistics for different countries around the world 
                and highlight differences between countries based on different comparators. 

                *Please click the tabs on the sidebar on the left to see visualisations
                for different categories of information*.
                """)
    st.image(
        'data/map of the world 4.png', 
        # width=1000
        use_column_width='auto'
    )
    st.markdown(f"""
                ## Data Sources
                The data for this dashboard was obtained from the following sources:
                
                ### Dataset 1: Life expectancy vs health expenditure, 2021                
                Link: https://ourworldindata.org/grapher/life-expectancy-vs-health-expenditure
                """)
    param_showDataset = st.checkbox(label='Show dataset')
    if param_showDataset:
        st.write(df1)
    st.markdown(f"""
                ### Dataset 2: Global Country Information Dataset 2023
                Link: https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023?resource=download
                """)
    param_showDataset2 = st.checkbox(label='Show dataset 2')
    if param_showDataset2:
        st.write(df2)


if __name__ == "__main__":
    if utils.authorisation():
        homepage('who???')