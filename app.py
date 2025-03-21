import streamlit as st
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import requests
from routes import getRouteTime
from destinations import destinations
from weather import getCurrentWeather



# if os.getenv("STREAMLIT_ENV") != "production":
#     load_dotenv()
load_dotenv()


st.title("SnowStake")

resorts = [resorts for resorts in destinations]
resorts = ["Select a resort"]+ resorts
chooseResort = st.selectbox('Where would you like to shred?', resorts)

if chooseResort != "Select a resort":
    # st.write(chooseResort)
    st.subheader(chooseResort)
    st.write(getRouteTime(chooseResort))
    st.write(getCurrentWeather(chooseResort))
    
# for dests in destinations: 
#     st.write(f"{dests}:")
#     st.write(getRouteTime(dests))
#     st.write(getCurrentWeather(dests))
#     st.write("")

