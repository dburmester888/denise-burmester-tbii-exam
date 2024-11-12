import streamlit as st
from generate_qrcode_page import generate_qrcode_page

# set up the page
st.set_page_config(page_title="My QR Code app",
                   page_icon="😊")

#directs a side bar with different pages
options =['Generate QR CODE', "Decode QR Code", 'About me']
page_selection = st.sidebar.selectbox("Menu", options)

#
if page_selection == "Generate QR CODE":
    generate_qrcode_page()
elif page_selection == "Decode QR Code":
    st.write("We will work on this")
elif page_selection == "About me":
    st.write("My name is Denise 😊")
