import streamlit as st
from streamlit_extras.colored_header import colored_header

from utilities import load_css, st_image
from PIL import Image

###### Page configuration
st.set_page_config(page_title='Streamlit Resources Library', page_icon='🍎')

###### Page logo and title
st.title("📚 Streamlit Resources Library")
st.sidebar.image('app/static/logo.png', height=100)
st.sidebar.markdown('''### About
''')

##### Teaching materials
colored_header(
  label='Teaching materials',
  description='A collection of materials that you can use for teaching Streamlit.',
  color_name='light-blue-70',
)

a1, a2, a3 = st.columns(3)

with a1:
  st.markdown('#### Streamlit 101 deck')
  st_image('https://101-deck.streamlit.app', 'app/static/streamlit-101-deck.png')
  st.info('An introductory deck on Streamlit that you can use to jump start your own lesson.')
  st.markdown('''
    [Google Slides](https://docs.google.com/presentation/d/1mL1HPJGBNg46pITigWyCXQbaG7AyAhKe8pNrwdy3u5M/edit?usp=sharing)
    |
    [Streamlit App](https://101-deck.streamlit.app)
  ''')
  
  
##### Learning materials
colored_header(
  label='Learning materials',
  description='A compilation of Streamlit learning materials.',
  color_name='light-blue-70',
)

b1, b2, b3 = st.columns(3)
b4, b5, b6 = st.columns(3)

with b1:
  st.markdown('#### 30 Days of Streamlit')
  st_image('', 'app/static/30DaysOfStreamlit.png')
  st.info('A 30-day social challenge for you to learn, build and deploy Streamlit apps.')
  st.markdown('''
    [Blog](https://blog.streamlit.io/30-days-of-streamlit/)
    |
    [Streamlit App](https://30days.streamlit.app/)''')
with b2:
  st.markdown('#### Streamlit Quests')
  st_image('', 'app/static/Streamlit-Quests.png')
  st.info("Here's a guided path for getting started with Streamlit.")
  st.markdown('[Blog](https://blog.streamlit.io/streamlit-quests-getting-started-with-streamlit/)')

with b3:
  st.markdown('#### Streamlit Documentation')
  st_image('', 'app/static/Streamlit-Documentation.png')
  st.info('A comprehensive documentation of the Streamlit library.')
  st.markdown('''
  [Documentation](https://docs.streamlit.io/)
  ''')
with b4:
  st.markdown('#### Streamlit Cheat Sheet')
  st_image('', 'app/static/Streamlit-Cheat-Sheet.png')
  st.info('A comprehensive summary of all Streamlit methods in this 1 page app.')
  st.markdown('''
  [Streamlit App](https://docs.streamlit.io/library/cheatsheet)
  ''')

  
##### Tutorials
colored_header(
  label='Tutorials',
  description='A curated list of essential Streamlit tutorials.',
  color_name='light-blue-70',
)

c1, c2, c3 = st.columns(3)
  
with c1:
  st.markdown('#### How to master Streamlit for data science')
  st_image('', 'app/static/Master-Streamlit-for-Data-Science.png')
  st.warning('This article shows you how to master Streamlit when getting started with data science.')
with c2:
  st.markdown('#### How to host app for free on Streamlit Community Cloud')
  st_image('', 'app/static/Host-Streamlit-App.png')
  st.warning('Learn how to transfer your apps from paid platforms to Streamlit Community Cloud.')
with c3:
  st.markdown('#### How to create interactive books with Streamlit')
  st_image('', 'app/static/Streamlit-Book.png')
  st.warning('Use streamlit_book library to create interactive books and presentations')
  
  
##### Images
colored_header(
  label='Images',
  description='A collection of Streamlit branding assets.',
  color_name='light-blue-70',
)

d1, d2, d3 = st.columns(3)

with d1:
  st.markdown('#### Streamlit Brand')
  st_image('https://streamlit.io/brand', 'app/static/streamlit-brand.png')
  st.warning('A collection of Streamlit logo.')
  st.markdown('[Website](https://streamlit.io/brand)')
with d2:
  st.markdown('#### Placeholder')
  st_image('', 'app/static/streamlit-placeholder.png')
  st.warning('A description of the resource.')
with d3:
  st.markdown('#### Placeholder')
  st_image('', 'app/static/streamlit-placeholder.png')
  st.warning('A description of the resource.')

  
##### Tools
colored_header(
  label='Tools',
  description='A list of essential Streamlit tools.',
  color_name='light-blue-70',
)

e1, e2, e3 = st.columns(3)

with e1:
  st.markdown('#### Streamlit Components Hub')
  st_image('', 'app/static/Streamlit-Components-Hub.png')
  st.warning('A collection of all Streamlit components aggregated from Github, PyPI, and the Streamlit forum.')
  st.markdown('[Streamlit App](https://components.streamlit.app/)')
with e2:
  st.markdown('#### Streamlit-Extras component')
  st_image('', 'app/static/Streamlit-Extras.png')
  st.warning('A Streamlit component that extend the native capabilities of Streamlit apps.')
  st.markdown('''
  [Blog](https://blog.streamlit.io/discover-and-share-useful-bits-of-code-with-the-streamlit-extras-library/)
  |
  [Streamlit App](https://extras.streamlit.app/)
  ''')
with e3:
  st.markdown('#### Streamlit-Faker component')
  st_image('', 'app/static/Streamlit-Faker.png')
  st.warning('A Streamlit component that allows you to quickly prototype a Streamlit app (think *Lorem ipsum* for Streamlit).')
  st.markdown('''
  [GitHub](https://github.com/arnaudmiribel/streamlit-faker)
  |
  [Streamlit App](https://fakker.streamlit.app/)
  |
  [YouTube Tutorial](https://youtu.be/zvWhdcpPJJg)
  ''')
  
load_css()
