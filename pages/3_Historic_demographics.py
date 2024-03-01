import streamlit as st
import pandas as pd
import seaborn as sns
import plotly_express as px
import streamlit_authenticator as stauth
import yaml #PyYAML
from yaml.loader import SafeLoader

from packages import utils, utils_plots

st.set_page_config(
    page_title='Multipage App',
    page_icon='👋',
    layout="wide"
)

def mainf():
    df1, df2 = utils.load_datasets()
    ### Sidebar
    st.sidebar.header('Parameters')
    param_analyseWhat = st.sidebar.radio(
        label='Choose what to analyse:',
        options=['Population', 'Life Expectancy', 'Health Expenditure'],
        index=0
    )
    df1 = df1.dropna(subset=param_analyseWhat)
    print(df1.columns)
    param_multiselect = st.sidebar.multiselect(label = 'Select countries:', 
                                            #    options=df1['Country'].unique(),
                                               options = df1.dropna(subset=param_analyseWhat)['Country'].unique(),
                                            #    default = ['Russia', 'USA', 'Mexico']
                                                default = ['Mexico', 'USA']
                                               )
    #

    df1_lifeExp = df1[df1['Country'].isin(param_multiselect)].reset_index()
    MIN, MAX = df1_lifeExp['Year'].min(), df1_lifeExp['Year'].max()
    if MIN < 0:
        MIN = 0
    #
    abcd = list(range(MIN, MAX+1))
    value1, value2 = st.sidebar.select_slider(
        "Choose the year range:", 
        # [0, 1, 2, 3, 4, 5],
        abcd, [MIN, MAX]
        # [-10000, -9999, -9998, -9997, -9996], [-10000, -9996]
        )
    print(value1, value2)
    # ### Main block
    st.markdown("""
                Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. Curabitur a sapien id tellus vestibulum scelerisque vitae vitae mi. Donec rhoncus dignissim pulvinar. Aenean ut ex in lectus porta consectetur. 
                
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ipsum mauris, porta vel facilisis in, iaculis at orci. Sed vitae aliquam velit. Nulla ornare magna vel lacus congue lobortis. Duis id suscipit tortor."""
                )  
    fig = utils_plots.lineplot_historic_demographics(df1_lifeExp, param_analyseWhat, value1, value2)
    st.plotly_chart(fig, use_container_width=True)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

if utils.authorisation():
    mainf()