import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
import yaml #PyYAML
import numpy as np
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
        choice1 = st.selectbox("Pick one", NUMERIC_COLUMNS)
        print(choice1)
    with c2:
        choice2 = st.selectbox("Pick oned", NUMERIC_COLUMNS)
    st.markdown("""---""")
    ### scatterplot
    fig = px.scatter(
        df2, x=choice1, y=choice2,
        log_x = True,
        log_y = True
    )
    st.plotly_chart(fig, use_container_width=True)
    fig = px.scatter(
        df2, x=choice1, y=choice2,
        # log_x = True,
        # log_y = True
    )
    st.plotly_chart(fig, use_container_width=True)



if __name__ == "__main__":
    if utils.authorisation():
        homepage('who???')