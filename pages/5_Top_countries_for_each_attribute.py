import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
import yaml #PyYAML
import numpy as np
from yaml.loader import SafeLoader

from packages import utils, utils_plots


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(
    page_title='Multipage App',
    page_icon='👋',
    layout="wide"
)

def homepage(username):
    df1, df2 = utils.load_datasets()
    print()
    NUMERIC_COLUMNS = df2.select_dtypes(include=np.number).columns.tolist()
    NUMERIC_COLUMNS = [i for i in NUMERIC_COLUMNS if i not in ['Latitude', 'Longitude']]
    print(NUMERIC_COLUMNS)
    ######################################################################################################################
    ##### Parameters #####################################################################################################
    ######################################################################################################################
    st.markdown("""---""")
    c1, c2 = st.columns(2, gap='large')
    with c1:
        choice = st.selectbox("Pick one", NUMERIC_COLUMNS)
        print(choice)
    with c2:
        howManyCountries = st.select_slider('How many countries?', [i for i in range(1, len(df2))], value=10)
    st.markdown("""---""")
    ### barplot top 10 highest
    largest10 = df2.nlargest(howManyCountries, choice)
    print(largest10)
    fig = px.bar(
        largest10, 
        x='Country', 
        y=choice,
        title=f'Top {howManyCountries} highest countries by {choice}'
    )
    st.plotly_chart(fig, use_container_width=True)
    ### barplot top 10 lowest
    lowest10 = df2.nsmallest(howManyCountries, choice).sort_values(by='Density (P/Km2)', ascending=True)
    print(lowest10)
    fig = px.bar(
        lowest10, 
        x='Country', 
        y=choice,
        title=f'Top {howManyCountries} lowest countries by {choice}'
    )
    st.plotly_chart(fig, use_container_width=True)
    ### boxplot distribution
    fig = px.box(
        df2, 
        x=choice,
        points='all',
        hover_data = ['Country', choice],
        title=f"Distribution boxplot of all countries by {choice}"
        )
    st.plotly_chart(fig, use_container_width=True)





if __name__ == "__main__":
    if utils.authorisation():
        homepage('who???')