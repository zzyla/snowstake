import streamlit as st
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import requests
from routes import getRoute
from destinations import destinations



# if os.getenv("STREAMLIT_ENV") != "production":
#     load_dotenv()
load_dotenv()


st.title("SnowStake")

for dests in destinations: 
    st.write(f"{dests}:")
    st.write(f"Time to:", getRoute(dests))
    st.write("")

