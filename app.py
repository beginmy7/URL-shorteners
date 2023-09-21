import streamlit as st
import pyshorteners as pyst

st.markdown("<h1 style='text-align: center;'>🔗URL Shortener</h1>", unsafe_allow_html=True)
st.write("<p style='text-align: center;'>Crafted by Izatcrust ✨</p>", unsafe_allow_html=True)

shortner=pyst.Shortener()

form=st.form("name")
url=form.text_input("URL Here")
s_btn=form.form_submit_button("Shorten it")

if s_btn:
    shorted_url=shortner.tinyurl.short(url)
    m = st.code(shorted_url)
    st.markdown("<p style='text-align: right;'>Copy  👆</p>", unsafe_allow_html=True)

if s_btn:
    st.balloons()

