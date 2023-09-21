import streamlit as st
import pyshorteners

st.title("<h1 style= 'text-align: center;'>🔗URL Shortener"</h1>, unsafe_allow_html=True)
st.write("Crafted by Izatcrust ✨")
st.divider()

s = pyshorteners.Shortener()
long_url = st.form("URL Here")
enter = st.button("Perpendek link")

m = s.tinyurl.short(long_url)
short_url = st.code(m)
st.markdown("Klik tombol salin di paling kanan")

if enter:
    st.balloons()
