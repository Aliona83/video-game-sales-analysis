import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load the dataset
df = pd.read_csv("data/vgchartz-2024.csv")

# Set up the Streamlit page
st.set_page_config(page_title="Video Game Sales Dashboard", layout="wide")

# Sidebar Navigation
st.sidebar.title("🎮 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Popular Consoles", "Most Popular Genres", "Sales Analysis", "Release Trends"])

# 🏠 Home Page