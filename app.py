# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("Hello2: Text")

st.title("Title: My first Streamlit App")

st.write("Hello, Streamlit!: Text")

st.header("Number selection: Header")

number = st.slider("Pick a number", 1, 100000)
st.write(f"You picked: {number}")