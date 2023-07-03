import io

import qrcode
import streamlit as st


def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color="black", back_color="white")
    return qr_image


st.title("QR Generator - akshar8460")

# User input
data_input = st.text_input("Enter the data to encode into the QR code")

if st.button("Generate QR Code"):
    if data_input:
        qr_code = generate_qr_code(data_input)

        # Convert the PIL Image to bytes
        image_bytes = io.BytesIO()
        qr_code.save(image_bytes, format='PNG')

        # Display the QR code image
        st.image(image_bytes, caption="QR Code", use_column_width=True)
    else:
        st.warning("Please enter some data.")
