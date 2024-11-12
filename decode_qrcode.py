import streamlit as st
import numpy as np
import cv2

st.header("DECODE THE QR CODE")

qrcode= st.file_uploader("Upload your QR Code",
type=['jpg'', 'png'', 'jpeg'])

#check you can place a qrcode
if qrcode:

# annoying code to convert the upload qrcode image into an image decoder

file_bytes= no.asarray(bytearray(qrcode.read())), dtype=no.vint8)
opencv_image= cv2.imdecode(file_bytes, 1)

#place the qr code
st.image(opencv_image),

# decode the qr code
detector = cv2.QRCodeDetector(),
decoded_info, point, straight_qr = detector.detectAndDecode(opencv.image)
st.write("YOUR QR CODE CONTAINED (decoded_info)")

# st.write(print)
#st.write(straight_orde_)