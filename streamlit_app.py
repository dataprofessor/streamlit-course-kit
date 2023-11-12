import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.app_logo import add_logo
from utilities import load_css, st_image
from PIL import Image

###### Page configuration
st.set_page_config(page_title='Streamlit Course Kit', layout='wide', page_icon='📦')

###### Page logo and title
st.title("📦 Streamlit Course Kit")
st.sidebar.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', use_column_width='always')
st.sidebar.markdown('''
### About
This **Streamlit Course Kit** is a collection of educational resources for helping you get started in using, teaching and creating content about [Streamlit](https://streamlit.io/).
''')

##### App templates
colored_header(
  label='App templates',
  description='Here are templates for building single page and multi-page Streamlit apps.',
  color_name='light-blue-70',
)

app_1, app_2, app_3 = st.columns(3)

with app_1:
  st.markdown('##### (Single-page) App starter kit')
  st_image('', 'app/static/Streamlit-app-starter-kit.png')
  st.info('Template for building a single page Streamlit app.')
  st.markdown('''
    [Blog](https://blog.streamlit.io/streamlit-app-starter-kit-how-to-build-apps-faster/)
    |
    [GitHub](https://github.com/streamlit/app-starter-kit)
  ''')

with app_2:
  st.markdown('##### Multi-page App starter kit')
  st_image('', 'app/static/Streamlit-multi-page-app-starter-kit.png')
  st.info('Template for building a multi-page Streamlit app.')
  st.markdown('''
    [GitHub](https://github.com/dataprofessor/st-multipage)
  ''')

##### Teaching materials
colored_header(
  label='Teaching materials',
  description='A collection of materials that you can use for teaching Streamlit.',
  color_name='light-blue-70',
)

teaching_1, teaching_2, teaching_3 = st.columns(3)

with teaching_1:
  st.markdown('##### Streamlit introductory slide deck')
  st_image('https://intro-deck.streamlit.app', 'app/static/Streamlit-intro-deck.png')
  st.info('An introductory deck on Streamlit that you can use to jump start your own lesson.')
  st.markdown('''
    [Google Slides](https://docs.google.com/presentation/d/1mL1HPJGBNg46pITigWyCXQbaG7AyAhKe8pNrwdy3u5M/edit?usp=sharing)
    |
    [Streamlit App](https://intro-deck.streamlit.app)
  ''')
  
  
##### Learning materials
colored_header(
  label='Learning materials',
  description='A compilation of Streamlit learning materials.',
  color_name='light-blue-70',
)

learning_1, learning_2, learning_3 = st.columns(3)
learning_4, learning_5, learning_6 = st.columns(3)

with learning_1:
  st.markdown('##### 30 Days of Streamlit')
  st_image('', 'app/static/30DaysOfStreamlit.png')
  st.info('A 30-day social challenge for you to learn, build and deploy Streamlit apps.')
  st.markdown('''
    [Blog](https://blog.streamlit.io/30-days-of-streamlit/)
    |
    [Streamlit App](https://30days.streamlit.app/)''')
with learning_2:
  st.markdown('##### Streamlit Quests')
  st_image('', 'app/static/Streamlit-Quests.png')
  st.info("Here's a guided path for getting started with Streamlit.")
  st.markdown('[Blog](https://blog.streamlit.io/streamlit-quests-getting-started-with-streamlit/)')

with learning_3:
  st.markdown('##### Streamlit Documentation')
  st_image('', 'app/static/Streamlit-Documentation.png')
  st.info('A comprehensive documentation of the Streamlit library.')
  st.markdown('''
  [Documentation](https://docs.streamlit.io/)
  ''')
with learning_4:
  st.markdown('##### Streamlit Cheat Sheet')
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

tutorials_1, tutorials_2, tutorials_3 = st.columns(3)
  
with tutorials_1:
  st.markdown('##### How to master Streamlit for data science')
  st_image('', 'app/static/Master-Streamlit-for-Data-Science.png')
  st.warning('This article shows you how to master Streamlit when getting started with data science.')
  st.markdown('[Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/)')
with tutorials_2:
  st.markdown('##### How to host app for free on Streamlit Community Cloud')
  st_image('', 'app/static/Host-Streamlit-App.png')
  st.warning('Learn how to transfer your apps from paid platforms to Streamlit Community Cloud.')
  st.markdown('[Blog](https://blog.streamlit.io/host-your-streamlit-app-for-free/)')
with tutorials_3:
  st.markdown('##### How to create interactive books with Streamlit')
  st_image('', 'app/static/Streamlit-Book.png')
  st.warning('Use streamlit_book library to create interactive books and presentations')
  st.markdown('[Blog](https://blog.streamlit.io/how-to-create-interactive-books-with-streamlit-and-streamlit-book-in-5-steps/)')
  
  
##### Images
colored_header(
  label='Images',
  description='A collection of Streamlit branding assets.',
  color_name='light-blue-70',
)

images_1, images_2, images_3 = st.columns(3)

with images_1:
  st.markdown('##### Streamlit Brand')
  st_image('https://streamlit.io/brand', 'app/static/Streamlit-brand.png')
  st.warning('A collection of Streamlit logo.')
  st.markdown('[Website](https://streamlit.io/brand)')
with images_2:
  st.markdown('##### Streamlit Cartoon')
  st_image('', 'app/static/Streamlit-Cartoon.png')
  st.warning('A collection of cartoon about Streamlit.')
  st.markdown('[GitHub repo](https://github.com/dataprofessor/streamlit-cartoon)')
#with images_3:
#  st.markdown('##### Placeholder')
#  st_image('', 'app/static/Streamlit-placeholder.png')
#  st.warning('A description of the resource.')

  
##### Tools
colored_header(
  label='Tools',
  description='A list of essential Streamlit tools.',
  color_name='light-blue-70',
)

st.markdown('#### :gray[Tools for content creation]')

tool_col = st.columns(3)


with tool_col[0]:
  st.markdown('##### App Screenshot')
  st_image('', 'app/static/App-Screenshot.png')
  st.warning('Captures the screenshot of a Streamlit app that can be used for multiple purposes especially as a Blog cover image.')
  st.markdown('[Streamlit App](https://screenshot.streamlit.app/)')
with tool_col[1]:
  st.markdown('##### Animated GIF Maker App')
  st_image('', 'app/static/Animated-GIF-Maker.png')
  st.warning('Converts a video file into an animated GIF file')
  st.markdown('''
  [Streamlit App](https://animated-gif.streamlit.app/)
  ''')
with tool_col[2]:
  st.markdown('##### Thumbnail Image Generator app')
  st_image('', 'app/static/Thumbnail-Image-Generator.png')
  st.warning('Automatically generates a thumbnail image that can be used for YouTube videos')
  st.markdown('''
  [Streamlit App](https://thumbnail-image.streamlit.app/)
  ''')


st.markdown('#### :gray[Tools for app building]')

tools_col = st.columns(3)

with tools_col[0]:
  st.markdown('##### Streamlit Components Hub')
  st_image('', 'app/static/Streamlit-Components-Hub.png')
  st.warning('A collection of all Streamlit components aggregated from Github, PyPI, and the Streamlit forum.')
  st.markdown('[Streamlit App](https://components.streamlit.app/)')
with tools_col[1]:
  st.markdown('##### Streamlit-Extras component')
  st_image('', 'app/static/Streamlit-Extras.png')
  st.warning('A Streamlit component that extend the native capabilities of Streamlit apps.')
  st.markdown('''
  [Blog](https://blog.streamlit.io/discover-and-share-useful-bits-of-code-with-the-streamlit-extras-library/)
  |
  [Streamlit App](https://extras.streamlit.app/)
  ''')
with tools_col[2]:
  st.markdown('##### Streamlit-Faker component')
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
