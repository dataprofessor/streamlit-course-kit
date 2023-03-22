import streamlit as st

def load_css():
  with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def st_image(link_input, image_input):
  return st.markdown(f'''
    <center>
    <a href="{link_input}">
      <img src="{image_input}" width="80%">
    </a>
    </center>''', unsafe_allow_html=True)
