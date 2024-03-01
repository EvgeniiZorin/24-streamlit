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
    choice = st.selectbox("Pick one", NUMERIC_COLUMNS)
    print(choice)
    asdf = df2.nlargest(10, choice)
    print(asdf)
    fig = px.bar(
        asdf, x='Country', y=choice
    )
    st.plotly_chart(fig, use_container_width=True)
    fig = px.box(df2, x=choice, points='all')
    st.plotly_chart(fig, use_container_width=True)





if __name__ == "__main__":
    if utils.authorisation():
        homepage('who???')