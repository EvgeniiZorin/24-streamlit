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
    df1, df2 = utils.load_datasets()
    print()
    NUMERIC_COLUMNS = df2.select_dtypes(include=np.number).columns.tolist()
    NUMERIC_COLUMNS = [i for i in NUMERIC_COLUMNS if i not in ['Latitude', 'Longitude']]
    print(NUMERIC_COLUMNS)
    ######################################################################################################################
    ##### Parameters #####################################################################################################
    ######################################################################################################################
    st.title('Two attribute scatterplot')
    st.markdown("""---""")
    c1, c2 = st.columns(2, gap='large')
    with c1:
        choice1 = st.selectbox("Pick a variable for the vertical axis", NUMERIC_COLUMNS)
        print(choice1)
    with c2:
        choice2 = st.selectbox("Pick a variable for the horisontal axis", NUMERIC_COLUMNS)
    st.markdown("""---""")
    ### normal scatterplot
    fig = px.scatter(
        df2, x=choice2, y=choice1,
        hover_data=['Country'],
        title=f'Scatterplot of {choice1} vs {choice2}'
    )
    st.plotly_chart(fig, use_container_width=True)
    ### log scatterplot
    fig = px.scatter(
        df2, x=choice2, y=choice1,
        hover_data=['Country'],
        log_x = True,
        log_y = True,
        title=f'Scatterplot (log base 10 transformed) of {choice1} vs {choice2}'
    )
    fig.update_layout(
        xaxis_title=f'{choice2} (log base 10 transformed)',
        yaxis_title=f'{choice1} (log base 10 transformed)'
    )
    st.plotly_chart(fig, use_container_width=True)




if __name__ == "__main__":
    if utils.authorisation():
        homepage('who???')