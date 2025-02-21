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
if page == "Home":
    st.title("🎮 Video Game Sales Analysis")
    st.write("Welcome to this interactive dashboard where we explore trends in video game sales!")

elif page == "Popular Consoles":
    st.title("🎮 Popular Consoles by Game Count")

# Count Games per console

    games_per_console = df['console'].value_counts()

    # Plotly Bar Char

    fig = px.bar(x=games_per_console.index, y=games_per_console.values,title="Number of Games per Console", labels={'x': 'Console', 'y': 'Number of Games'})
    st.plotly_chart(fig)

# 🎮 Most Popular Game Genres
elif page == "Most Popular Genres":
    st.title("🎮 Most Popular Game Genres")

    genre_sales = df.groupby('genre')['total_sales'].sum().sort_values(ascending=False)

    # Pie Chart
    fig = px.pie(values=genre_sales.values, names=genre_sales.index, title="Total Sales by Genre")
    st.plotly_chart(fig)

elif page == "Sales Analysis":
    st.title("💰 Sales Analysis by Region")

    # Select region for analysis
    region = st.selectbox("Select Region", ['total_sales', 'na_sales', 'jp_sales', 'pal_sales', 'other_sales'])

    # Top 10 best-selling games in the selected region
    top_games = df[['title', 'genre', region]].sort_values(by=region, ascending=False).head(10)

    # Combine Title & Genre for better visualization
    top_games["title & genre"] = top_games["title"] + " (" + top_games["genre"] + ")"

    # Create a bar chart
    fig = px.bar(
        top_games,
        x="title & genre",
        y=region,
        title=f"Top 10 Best-Selling Games in {region}",
        text=region,
        color="genre"
    )

    # Improve layout
    fig.update_layout(xaxis_title="Game (Genre)", yaxis_title="Sales (millions)", xaxis_tickangle=-45)

    st.plotly_chart(fig)
# elif page == "Sales Analysis":
#     st.title("🌍 Game Sales by Region")
#
#     # Summing total sales per region
#     regional_sales = {
#         "North America": df["na_sales"].sum(),
#         "Japan": df["jp_sales"].sum(),
#         "Europe (PAL)": df["pal_sales"].sum(),
#         "Other Regions": df["other_sales"].sum()
#     }
#
#     # Convert to DataFrame for Plotly
#     sales_df = pd.DataFrame(list(regional_sales.items()), columns=["Region", "Total Sales (millions)"])
#
#     # Create a bar chart with Plotly
#     fig = px.bar(sales_df, x="Region", y="Total Sales (millions)",
#                  title="Total Game Sales by Region",
#                  color="Region", text="Total Sales (millions)")
#
#     st.plotly_chart(fig)