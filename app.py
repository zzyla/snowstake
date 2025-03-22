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
from snowConditions import getsnowConditions, getForecast



# if os.getenv("STREAMLIT_ENV") != "production":
#     load_dotenv()
load_dotenv()


st.title("SnowStake")

resorts = [resorts for resorts in destinations]
resorts = ["Select a resort"]+ resorts
chooseResort = st.selectbox('Where would you like to shred?', resorts)

if chooseResort != "Select a resort":
    with st.container():
        st.header(chooseResort)
        
        row1_col1, row1_col2 = st.columns(2, border=True)
        with row1_col1:
            st.markdown("#### Travel")
            # st.write(getRouteTime(chooseResort))
            st.write("Google maps goes here")
        with row1_col2:
            st.markdown("#### Snow Conditions")
            # st.write(getsnowConditions(chooseResort)) # waiting for api to work
            # st.write(getForecast(chooseResort)) # waiting for api to work
            
        row2_col1, row2_col2 = st.columns(2, border=True)
        with row2_col1:
            st.markdown("#### Current Weather")
            st.write(getCurrentWeather(chooseResort))
        with row2_col2:
            st.markdown("#### Lift Status")
        
        
        st.info("Sumamrry goes here")
    
# for dests in destinations: 
#     st.write(f"{dests}:")
#     st.write(getRouteTime(dests))
#     st.write(getCurrentWeather(dests))
#     st.write("")

