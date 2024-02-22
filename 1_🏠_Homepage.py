import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
import yaml #PyYAML
from yaml.loader import SafeLoader


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

st.set_page_config(
    page_title='Multipage App',
    page_icon='👋'
)

def homepage(username):
    st.sidebar.write(f'*Welcome, {username}*')
    # st.sidebar.title(f"Welcome, {username}")
    # st.write(f'Welcome *{st.session_state["name"]}*')
    authenticator.logout("Logout", 'sidebar')
    st.title('My Dashboard')
    st.markdown('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a sapien id tellus vestibulum scelerisque vitae vitae mi. Donec rhoncus dignissim pulvinar. Aenean ut ex in lectus porta consectetur. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ipsum mauris, porta vel facilisis in, iaculis at orci. Sed vitae aliquam velit. Nulla ornare magna vel lacus congue lobortis. Duis id suscipit tortor.')

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


name, authentication_status, username = authenticator.login()
if authentication_status == False:
    st.error('Username/password is incorrect')
if authentication_status == None:
    st.warning('Please enter your username and password')
if authentication_status:
    homepage(username)

