import streamlit as st
import qrcode
from io import BytesIO

st.markdown("<h1 style='text-align: center; color: white;'>🌟 InstaQR 🌟</h1>", unsafe_allow_html=True)
st.markdown("##### Generate beautiful, customizable QR codes instantly!", unsafe_allow_html=True)

data=st.text_input("🔗 Enter the data (URL or Text) for QR Code:")

fill_color=st.color_picker("🎨 Pick QR Code Color (Dots):", "#ffffff")
back_color=st.color_picker("🎨 Pick Background Color:", "#ffffff")

if st.button("✨ Generate My QR Code"):
    if not data.strip():
        st.warning("⚠️ Please enter some data to generate QR Code.")
    else:
        qr = qrcode.QRCode(version=1,box_size=10,border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        buffer = BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)

        st.image(buffer, caption="🎉 Your QR Code is Ready!", use_container_width=True)

        st.download_button(
            label="📥 Download QR Code",
            data=buffer.getvalue(),
            file_name="qrcode.png",
            mime="image/png"
        )

        st.balloons()  # 🎈 Celebrate on QR generation
        st.toast('QR Code Generated Successfully! 🎉')
