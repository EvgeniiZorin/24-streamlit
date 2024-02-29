import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px

def barplot_demographics(df2_select, variable, sort_by, sort_how):
    if sort_by == "Each parameter's respective value":
        sort_by = variable
    sort_how_dict = {'Descending':True, 'Ascending':False}
    fig = px.bar(
        df2_select.sort_values(sort_by, ascending=sort_how_dict[sort_how]), ### always sort on Population column
        # x='Country', y='Population',
        x=variable, y='Country', orientation='h',
        # title=variable,
        text=variable
    )
    fig.update_traces(
        textposition='outside', 
        cliponaxis=False,
        texttemplate='%{text:,}',
        # textfont_size=100
    )
    a = df2_select[variable].max()
    print(a, type(a))
    fig.update_layout(
        yaxis_title='',
        xaxis_title='',
        title={
            'text': variable + '<br>',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        },
        xaxis_range=[0, a*1.55],
        title_font_size = 30,
        font_size = 20, # data callouts
        yaxis_tickfont_size = 25,
        xaxis_tickfont_size = 20,
        xaxis_title_font_size = 25,
        
    )
    return fig