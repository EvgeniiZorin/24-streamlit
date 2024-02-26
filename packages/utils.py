import streamlit as st

# State management -----------------------------------------------------------

# I like to use state instead of the long form 
state = st.session_state


def init_state(key, value):
  if key not in state:
    state[key] = value

init_state('login_successful', False)
init_state('username', '')
init_state('password', '')
print(state)
print(state.login_successful)

# generic callback to set state
def _set_state_cb(**kwargs):
    for state_key, widget_key in kwargs.items():
        val = state.get(widget_key, None)
        if val is not None or val == "":
            setattr(state, state_key, state[widget_key])

def _set_login_cb(username, password):
    state.login_successful = login(username, password)  

def _reset_login_cb():
    state.login_successful = False
    state.username = ""
    state.password = "" 

# print('a')
# init_state('login_successful', False)
# init_state('username', '')
# init_state('password', '')
# print(state.login_successful)
# -----------------------------------------------------------------------------

# Function to check login credentials
def login(username, password):
    return username == "a" and password == "b"

def main2():
    st.sidebar.button("Logout", on_click=_reset_login_cb)
    st.subheader("My Page")
    st.write("Hello")

# Main function
def authorisation():
    st.title("My App")
    state = st.session_state
    init_state('login_successful', False)
    init_state('username', '')
    init_state('password', '')
    # If login is successful, display "Hello"
    if state.login_successful:
        # st.button("Logout", on_click=_reset_login_cb)
        # main2()
        # print('Running function...')
        # function1()
        ###
        st.sidebar.subheader("utils.py")
        st.sidebar.button("Logout", on_click=_reset_login_cb)
        return True
    else:
        st.subheader("Login")
        # Display login form
        st.text_input(
            "Username:", value=state.username, key='username_input',
            on_change=_set_state_cb, kwargs={'username': 'username_input'}
        )
        st.text_input(
            "Password:", type="password", value=state.password, key='password_input',
            on_change=_set_state_cb, kwargs={'password': 'password_input'}
        )

        # st.write(state.username)
        # st.write(state.password)
        
        # Check login credentials
        if not state.login_successful and st.button("Login", on_click=_set_login_cb, args=(state.username, state.password)):
            st.warning("Wrong username or password.")

if __name__ == "__main__":
    # main()
    # main( main2() )
    print('Running "utils.py" on its own.')
    if authorisation():
        main2()

