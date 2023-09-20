import streamlit as st
import pyshorteners

st.title("URL Shortener")
st.write("Crafted by Izatcrust ✨")
st.divider()

s = pyshorteners.Shortener()
long_url = st.text_input("Masukkan link")
enter = st.button("Perpendek link")

m = s.tinyurl.short(long_url)
short_url = st.code(m)
st.markdown("Klik tombol salin di paling kanan")

if enter:
    st.balloons()
