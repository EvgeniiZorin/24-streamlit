import streamlit as st
import pandas as pd
import seaborn as sns
import plotly_express as px
import streamlit_authenticator as stauth
import yaml #PyYAML
from yaml.loader import SafeLoader

from packages import utils

st.set_page_config(
    page_title='Multipage App',
    page_icon='👋',
    layout="wide"
)

def countries(username):
    df1, df2 = utils.load_datasets()
    print('Datasets loaded!')
    ### Sidebar
    st.sidebar.write(f'*Welcome, {username}*')
    # st.sidebar.header('Dashboard `version 2`')
    st.sidebar.header('Parameters')
    param_showDataset = st.sidebar.checkbox(label='Show dataset')
    # param_person = st.sidebar.selectbox(label='Person', 
    #                                     options=df['Person'].unique())
    param_multiselect = st.sidebar.multiselect(label='Country', 
                                               options=df1['Country'].unique(),
                                               default=df1['Country'].unique())
    ### Main block
    st.title('Countries')
    st.markdown("""
                Lorem ipsum dolor sit amet, **consectetur** adipiscing elit. Curabitur a sapien id tellus vestibulum scelerisque vitae vitae mi. Donec rhoncus dignissim pulvinar. Aenean ut ex in lectus porta consectetur. 
                
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ipsum mauris, porta vel facilisis in, iaculis at orci. Sed vitae aliquam velit. Nulla ornare magna vel lacus congue lobortis. Duis id suscipit tortor.""")
    # st.write("""
    # # My first app
    # Hello *world!*
    # hello there!
    # """)
    # Read dataset
    
    # Display dataset
    if param_showDataset:
        st.write(df1)
    # ### Line chart with one person
    # df_slice1 = df[df['Person'] == param_person].reset_index()
    # st.line_chart(df_slice1, x='Period', y='Sales', color='Person')
    ###########################################################
    ##### Line chart with life expectancy per country #########
    ###########################################################
    # st.write("You chose: ", ', '.join(param_multiselect))
    df1_lifeExp = df1[df1['Country'].isin(param_multiselect)].reset_index()
    ### Streamlit
    # st.line_chart(df1_lifeExp, x='Year', y='Life_Expectancy', color='Country')
    ### Plotly
    fig = px.line(df1_lifeExp, x="Year", y="Life_Expectancy", title='Life expectancy in the selected countries over the period of 1970 - 2020',color='Country', hover_data = {'Country':False, 'Year':False})
    st.plotly_chart(fig, use_container_width=True)
    ### Seaborn
    # ab = sns.lineplot(
    #     x=df1_lifeExp['Year'], y=df1_lifeExp['Life_Expectancy'],
    #     hue=df1_lifeExp['Country']
    # )
    # st.pyplot(ab.get_figure())
    df2_select = df2[df2['Country'].isin(param_multiselect)].reset_index()


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

if utils.authorisation():
    countries('jack jones!!!')