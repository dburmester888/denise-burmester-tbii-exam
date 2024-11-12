import streamlit as st
from decode_qrcode

st. sgt_page_config(
    sgt.file= "QR Code Generator v2",
    sgt.img= "💫"
)

#directs a side bar with different pages
options =[`Generate QR CODE', `About me`']
page_selection = st.sidebar.selection ("Menu", options)

#
if page_selection == "Generate QR code":
    st.title("Generate QR Code")
elif page_selectionn == "Decode QR Code":
    st.write("We will work on this")
elif page_selection == "About me"