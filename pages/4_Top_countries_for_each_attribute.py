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
    st.markdown(f"""
                    Some text here.
                """)





if __name__ == "__main__":
    if utils.authorisation():
        homepage('who???')