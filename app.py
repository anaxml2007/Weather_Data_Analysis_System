import numpy as np
import pandas as pd
import streamlit as st

# Website Title
st.set_page_config(page_title="Thrissur Weather Dashboard", page_icon="🌤️")
st.title("🌤️ Thrissur Weather Analysis Dashboard (2025)")
st.write(
    "Welcome to the public weather monitoring dashboard for Thrissur, Kerala. Built with Python and Streamlit."
)

# 1. Dataset Configuration
months_names = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
weather_data = {
    "Month": months_names,
    "Max Temperature (°C)": [
        33.8,
        35.2,
        37.9,
        38.5,
        35.8,
        31.2,
        30.1,
        29.9,
        31.4,
        32.0,
        32.7,
        33.2,
    ],
    "Avg Temperature (°C)": [
        27.5,
        28.8,
        31.0,
        32.1,
        29.4,
        26.8,
        25.9,
        25.7,
        26.5,
        27.1,
        27.3,
        27.6,
    ],
    "Max Humidity (%)": [72, 70, 68, 74, 82, 96, 99, 97, 94, 89, 80, 75],
    "Avg Humidity (%)": [60, 56, 53, 59, 70, 85, 89, 87, 81, 75, 68, 63],
}
df = pd.DataFrame(weather_data)

# Interactive Checkbox for Table
if st.checkbox("Show Detailed Weather Dataset Table"):
    st.subheader("2025 Comprehensive Data")
    st.dataframe(df)

# 2. Temperature Line Chart
st.subheader("📈 Temperature Profile (Maximum vs Average)")
st.line_chart(df.set_index("Month")[["Max Temperature (°C)", "Avg Temperature (°C)"]])

# 3. Humidity Bar Chart
st.subheader("💧 Humidity Profile (Maximum vs Average)")
st.bar_chart(df.set_index("Month")[["Max Humidity (%)", "Avg Humidity (%)"]])

st.caption("Data Source: Historical Analysis | Project Dashboard by Anax")
