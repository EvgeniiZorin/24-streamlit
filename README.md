

# Name of Streamlit App

Description of the app ...

# Demo App

<!-- [![Streamlit App](<https://static.streamlit.io/badges/streamlit_badge_black_white.svg>)](<https://test-dashboard-1.streamlit.app/>) -->

https://test-dashboard-1.streamlit.app/

# Section Heading

This is filler text. Please replace this with the text for this section.

# Further Reading

This is filler text. Please replace this with explanatory text about further relevant resources for this repo.
- Resource 1
- Resource 2
- Resource 3

<!-- some comments here -->


<!-- Starter set:
https://blog.streamlit.io/streamlit-app-starter-kit-how-to-build-apps-faster/ -->


# Code

Run locally by installing conda venv, then running:
```powershell
streamlit run main.py
```

# Data

dataset 1:
seaborn `sns.load_dataset('healthexp')`

dataset 2:
Global Country Information Dataset 2023
https://www.kaggle.com/datasets/nelgiriyewithana/countries-of-the-world-2023?resource=download


# Notes (for development)

## Authentication

In version 1, did the following way. Problem - upon hosting it online, login and logout buttons had to be pressed twice. 

```py
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


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

```

Solved by rewriting the authentication as per https://discuss.streamlit.io/t/streamlit-login-solution-need-to-click-on-login-button-twice-to-login/57336/2. 
