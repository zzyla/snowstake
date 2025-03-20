import streamlit as st
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv
import requests
from routes import getRoute


# if os.getenv("STREAMLIT_ENV") != "production":
#     load_dotenv()
load_dotenv()


st.title("SnowStake")

st.write("Time to Copper Mountain:", getRoute())


