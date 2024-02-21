import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml #PyYAML
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

def read_dataset():
    df = pd.read_csv("my_data.csv")
    return df

def main_vis(username):
    df = read_dataset()
    ### Sidebar
    st.sidebar.title(f"Welcome, {username}")
    st.sidebar.header('Dashboard `version 2`')
    st.sidebar.subheader('Parameter 1')
    param_showDataset = st.sidebar.checkbox(label='Show dataset')
    # param_person = st.sidebar.selectbox(label='Person', 
    #                                     options=df['Person'].unique())
    param_multiPerson = st.sidebar.multiselect(label='Person', 
                                          options=df['Person'].unique(),
                                          default=df['Person'].unique())
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
        st.write("Data:")
        st.write(df)
    # ### Line chart with one person
    # df_slice1 = df[df['Person'] == param_person].reset_index()
    # st.line_chart(df_slice1, x='Period', y='Sales', color='Person')
    ### Line chart with many people
    st.write("You chose: ", ', '.join(param_multiPerson))
    df_slice = df[df['Person'].isin(param_multiPerson)].reset_index()
    print(df_slice)
    st.line_chart(df_slice, x='Period', y='Sales', color='Person')
    #
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

