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
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Popular Consoles", "Most Popular Genres", "Sales Analysis", "Game Developers"])

# Home Page
if page == "Home":
    st.title("Video Game Sales Analysis")
    st.write("Welcome to this interactive dashboard where we explore trends in video game sales!")

elif page == "Popular Consoles":
    st.title("🎮 Popular Consoles by Game Count")

# Count Games per console

    games_per_console = df['console'].value_counts()

    # Plotly Bar Char

    fig = px.bar(x=games_per_console.index, y=games_per_console.values,title="Number of Games per Console", labels={'x': 'Console', 'y': 'Number of Games'})
    st.plotly_chart(fig)

# Most Popular Game Genres
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

elif page == "Game Developers":
    st.title("Top 15 Best-Selling Developers")

    # Filter out rows where 'developer' or 'total_sales' are NaN
    df_filtered = df[df['developer'].notna() & df['total_sales'].notna()]

    # Find the best-selling game for each developer
    best_game_idx = df_filtered.groupby('developer')['total_sales'].idxmax()

    # Extract the corresponding game title and sales
    best_developer = df_filtered.loc[best_game_idx, ['developer', 'title', 'total_sales']]

    # Sort by total sales in descending order and keep only the top 15 developers
    top_15_developers = best_developer.sort_values(by='total_sales', ascending=False).head(15)

    # Create a bar chart for the top 15 developers
    fig = px.bar(top_15_developers, x="developer", y="total_sales", color="title",
                 title="Top 15 Best-Selling Developers")

    # Improve layout
    fig.update_layout(xaxis_title="Developer", yaxis_title="Total Sales (millions)", xaxis_tickangle=-45)

    st.plotly_chart(fig)
