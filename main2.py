import pandas as pd
import seaborn as sns
import plotly.express as px
import streamlit as st
import streamlit_authenticator as stauth
import yaml #PyYAML
from yaml.loader import SafeLoader

sns.set_style('whitegrid', {
    'axes.grid': False,
    'axes.spines.left': False, 
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.spines.bottom': False
    })

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

def read_dataset():
    df = pd.read_csv("my_data.csv")
    return df

def load_datasets():
    ### dataset 1
    df1 = sns.load_dataset('healthexp')
    df1['Country'] = df1['Country'].replace({'Great Britain':'United Kingdom'})
    ### dataset 2
    df2 = pd.read_csv('data/world-data-2023.csv')
    df2['Country'] = df2['Country'].replace({'United States':'USA'})
    return df1, df2

def main_vis(username):
    df1, df2 = load_datasets()
    ### Sidebar
    st.sidebar.title(f"Welcome, {username}")
    st.sidebar.header('Dashboard `version 2`')
    st.sidebar.subheader('Parameter 1')
    param_showDataset = st.sidebar.checkbox(label='Show dataset')
    # param_person = st.sidebar.selectbox(label='Person', 
    #                                     options=df['Person'].unique())
    param_multiselect = st.sidebar.multiselect(label='Country', 
                                               options=df1['Country'].unique(),
                                               default=df1['Country'].unique())
    ### Main block
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    st.write("""
    # My first app
    Hello *world!*
    hello there!
    """)
    # Read dataset
    
    # Display dataset
    if param_showDataset:
        c1, c2 = st.columns(2)
        with c1:
            st.write('Dataset 1:')
            st.write(df1)
        with c2:
            st.write('Dataset 2:')
            st.write(df2)
    # ### Line chart with one person
    # df_slice1 = df[df['Person'] == param_person].reset_index()
    # st.line_chart(df_slice1, x='Period', y='Sales', color='Person')
    ###########################################################
    ##### Line chart with life expectancy per country #########
    ###########################################################
    st.write("You chose: ", ', '.join(param_multiselect))
    df1_lifeExp = df1[df1['Country'].isin(param_multiselect)].reset_index()
    ### Streamlit
    # st.line_chart(df1_lifeExp, x='Year', y='Life_Expectancy', color='Country')
    ### Plotly
    fig = px.line(df1_lifeExp, x="Year", y="Life_Expectancy", title='Life expectancy in the selected countries',color='Country', hover_data = {'Country':False, 'Year':False})
    st.plotly_chart(fig, use_container_width=True)
    ### Seaborn
    # ab = sns.lineplot(
    #     x=df1_lifeExp['Year'], y=df1_lifeExp['Life_Expectancy'],
    #     hue=df1_lifeExp['Country']
    # )
    # st.pyplot(ab.get_figure())
    ###########################################################
    ##### Bar chart with population per country ###############
    ###########################################################
    df2_select = df2[df2['Country'].isin(param_multiselect)].reset_index()
    fig = px.bar(
        df2_select, x='Country', y='Population',
        title = 'Population in the selected countries'
    )
    st.plotly_chart(fig, use_container_width=True)
    ### Some text here
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
                    ### Column 1
                    
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur a sapien id tellus vestibulum scelerisque vitae vitae mi. Donec rhoncus dignissim pulvinar. Aenean ut ex in lectus porta consectetur. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse ipsum mauris, porta vel facilisis in, iaculis at orci. Sed vitae aliquam velit. Nulla ornare magna vel lacus congue lobortis. Duis id suscipit tortor.
                    """)
    with c2:
        st.markdown("""
                    ### Column 2

                    Sed sem odio, egestas vel convallis sit amet, facilisis quis leo. Suspendisse potenti. In hac habitasse platea dictumst. Sed consectetur ut erat viverra cursus. Quisque volutpat leo a mollis ullamcorper. Phasellus pretium, massa sit amet dapibus lobortis, arcu purus accumsan odio, a finibus ante ante in erat. Etiam sed justo nec justo vestibulum porttitor ac quis ipsum. Fusce vel molestie risus. Mauris ultrices ex nisi, et sollicitudin tortor lobortis at. In sed mauris at ipsum mollis gravida at sit amet sem. Cras lobortis metus et lacus eleifend convallis. Morbi venenatis enim dictum est venenatis ultrices.
                    """)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


"""
AUTHENTICATION
""";
# authenticator.login()
# if st.session_state["authentication_status"]:
#     authenticator.logout()
#     main_vis()
# elif st.session_state["authentication_status"] is False:
#     st.error('Username/password is incorrect')
# elif st.session_state["authentication_status"] is None:
#     st.warning('Please enter your username and password')


name, authentication_status, username = authenticator.login()
if authentication_status == False:
    st.error('Username/password is incorrect')
if authentication_status == None:
    st.warning('Please enter your username and password')
if authentication_status:
    authenticator.logout("Logout", 'sidebar')
    main_vis(username)

