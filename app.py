import streamlit as st
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import os
from dotenv import load_dotenv


# if os.getenv("STREAMLIT_ENV") != "production":
#     load_dotenv()
load_dotenv()

GOOGLE_MAPS_KEY = os.getenv("GOOGLE_MAPS_KEY")


st.title("SnowStake")




