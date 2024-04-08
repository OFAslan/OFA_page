import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()


col1, col2, col3 = st.columns(3)
col2.image(Image.open('photo.png'))

col2.header("OGUZHAN FURKAN ASLAN", style={"font-size": "40px"})

st.info('Data & Analytics Specialist, Data Engineer')

icon_size = 23

st_button('medium', 'https://medium.com/@furkan-aslan', 'Read my Blogs', icon_size) 
st_button('linkedin', 'https://www.linkedin.com/in/oguzhanaslan3707/', 'Connect with me on LinkedIn', icon_size)
st_button('github', 'https://github.com/OFAslan', 'My Github Link', icon_size)
