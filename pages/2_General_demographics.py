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

def countries(username):
    df1, df2 = utils.load_datasets()
    ##############################################
    ##### Sidebar ################################
    ##############################################
    st.sidebar.header('Parameters')
    param_multiselect = st.sidebar.multiselect(
        label='Select countries:', 
        options=df2['Country'].unique(),
        # default=df2['Country'].unique()
        default=['Mexico', 'USA', 'Germany']
    )
    param_sortHow = st.sidebar.radio(
        label='Sort all plots in the order:',
        options=['Descending', 'Ascending']
    )
    param_sortBy = st.sidebar.radio(
        label='Sort all plots by:', 
        options=['Population', 'Land Area(Km2)', 'Density (P/Km2)', 'Birth Rate', "Each parameter's respective value"],
        index=0
    )
    print(param_sortBy)
    ### Main block
    st.markdown("""
                Here you will see bar plots for different statistics for 
                selected countries. On all barplots, countries are sorted 
                by population in descending order. 

                *Please choose countries on the sidebar on the left to show demographic statistics.*
                """)
    # ### Line chart with one person
    # df_slice1 = df[df['Person'] == param_person].reset_index()
    # st.line_chart(df_slice1, x='Period', y='Sales', color='Person')
    df2_select = df2[df2['Country'].isin(param_multiselect)].reset_index()
    c1, c2 = st.columns(2)
    with c1:
        fig = utils_plots.barplot_demographics(df2_select, 'Population', param_sortBy, param_sortHow)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        # fig = utils_plots.barplot_demographics(df2_select, 'Density (P/Km2)')
        # st.plotly_chart(fig, use_container_width=True)
        # st.write('a')
        pass
    c1, c2 = st.columns(2)
    with c1:
        fig = utils_plots.barplot_demographics(df2_select, 'Land Area(Km2)', param_sortBy, param_sortHow)
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        fig = utils_plots.barplot_demographics(df2_select, 'Density (P/Km2)', param_sortBy, param_sortHow)
        st.plotly_chart(fig, use_container_width=True)
    c1, c2 = st.columns(2)
    with c1:
        # st.markdown("""Definition of birth rate""")
        fig = utils_plots.barplot_demographics(df2_select, 'Birth Rate', param_sortBy, param_sortHow)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
                    ***Birth Rate**: The total number of births in a year per 1,000 individuals.*
                    """)
    with c2:
        fig = utils_plots.barplot_demographics(df2_select, 'Fertility Rate', param_sortBy, param_sortHow)
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("""
                    ***Fertility Rate**: 
                    The total fertility rate in a specific year is defined as the 
                    total number of children that would be born to each woman if she 
                    were to live to the end of her child-bearing years and give birth to 
                    children in alignment with the prevailing age-specific fertility 
                    rates. (https://data.oecd.org/pop/fertility-rates.htm)*
                    """)


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

if utils.authorisation():
    countries('jack jones!!!')