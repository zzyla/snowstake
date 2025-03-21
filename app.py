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

for dests in destinations: 
    st.write(f"{dests}:")
    st.write(getRouteTime(dests))
    st.write(getCurrentWeather(dests))
    st.write("")

