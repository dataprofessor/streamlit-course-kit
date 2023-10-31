import streamlit as st

st.title('Redirecting to the Streamlit Course Kit')

st.write('https://course-kit.streamlit.app/')

def nav_to(url):
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    st.write(nav_script, unsafe_allow_html=True)

nav_to('https://course-kit.streamlit.app/')
