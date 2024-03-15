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
    # ### Sidebar
    # st.sidebar.header('Parameters')
    # param_analyseWhat = st.sidebar.radio(
    #     label='Choose what to analyse:',
    #     options=['Population', 'Life Expectancy', 'Health Expenditure'],
    #     index=0
    # )
    # # st.write(df1.columns)
    # df1 = df1.dropna(subset=param_analyseWhat)
    # print(df1.columns)
    # param_multiselect = st.sidebar.multiselect(label = 'Select countries:', 
    #                                         #    options=df1['Country'].unique(),
    #                                            options = df1.dropna(subset=param_analyseWhat)['Country'].unique(),
    #                                         #    default = ['Russia', 'USA', 'Mexico']
    #                                             default = ['Mexico', 'USA']
    #                                            )
    # #

    st.markdown("""
                Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. Curabitur a sapien id tellus vestibulum scelerisque vitae vitae mi. Donec rhoncus dignissim pulvinar. Aenean ut ex in lectus porta consectetur. 
                
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ipsum mauris, porta vel facilisis in, iaculis at orci. Sed vitae aliquam velit. Nulla ornare magna vel lacus congue lobortis. Duis id suscipit tortor."""
                )
    ######################################################################################################################
    ##### Parameters #####################################################################################################
    ######################################################################################################################
    st.markdown("""---""")
    # st.header('Parameters')
    c1, c2, c3 = st.columns(3, gap='large')
    with c1:
        param_analyseWhat = st.radio(
            label='Choose what to analyse:',
            options=['Population', 'Life Expectancy', 'Health Expenditure'],
            index=0
        )
    # st.write(df1.columns)
    df1 = df1.dropna(subset=param_analyseWhat)
    print(df1.columns)
    with c2:
        param_multiselect = st.multiselect(label = 'Select countries:', 
                                                #    options=df1['Country'].unique(),
                                                options = df1.dropna(subset=param_analyseWhat)['Country'].unique(),
                                                #    default = ['Russia', 'USA', 'Mexico']
                                                    default = ['Mexico', 'USA']
                                                )


    df1_lifeExp = df1[df1['Country'].isin(param_multiselect)].reset_index()
    MIN, MAX = df1_lifeExp['Year'].min(), df1_lifeExp['Year'].max()
    if MIN < 1000:
        MIN = 1000
    #
    abcd = list(range(MIN, MAX+1))
    with c3:
        value1, value2 = st.select_slider(
            "Choose the year range:", 
            # [0, 1, 2, 3, 4, 5],
            abcd, [MIN, MAX]
            # [-10000, -9999, -9998, -9997, -9996], [-10000, -9996]
            )
    print(value1, value2)
    st.markdown("""---""")

    # ### Main block

    fig = utils_plots.lineplot_historic_demographics(df1_lifeExp, param_analyseWhat, value1, value2)
    st.plotly_chart(fig, use_container_width=True)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

if utils.authorisation():
    mainf()