import streamlit as st
import pandas as pd
import pickle


# =========================
# Load trained model
# =========================

@st.cache_resource
def load_model():

    with open("xgboost_demand_pipeline.pkl", "rb") as f:
        model = pickle.load(f)

    return model


model = load_model()


# =========================
# App title
# =========================

st.title("Demand Forecasting App")

st.divider()

st.header("Input Features")


# =========================
# User inputs
# =========================

price = st.number_input(
    "Price",
    min_value=0.0,
    value=50.0
)

discount = st.number_input(
    "Discount (%)",
    min_value=0,
    max_value=100,
    value=10
)

inventory_level = st.number_input(
    "Inventory Level",
    min_value=0,
    value=100
)

promotion = st.selectbox(
    "Promotion",
    [0, 1]
)

competitor_pricing = st.number_input(
    "Competitor Price",
    min_value=0.0,
    value=50.0
)

category = st.selectbox(
    "Category",
    [
        "Electronics",
        "Clothing",
        "Groceries",
        "Toys",
        "Furniture"
    ]
)

region = st.selectbox(
    "Region",
    [
        "North",
        "South",
        "East",
        "West"
    ]
)

weather = st.selectbox(
    "Weather Condition",
    [
        "Snowy",
        "Cloudy",
        "Sunny",
        "Rainy"
    ]
)

seasonality = st.selectbox(
    "Seasonality",
    [
        "Winter",
        "Spring",
        "Summer",
        "Autumn"
    ]
)

epidemic = st.selectbox(
    "Epidemic",
    [0, 1]
)


# =========================
# Date features
# =========================

st.subheader("Date Information")

year = st.number_input(
    "Year",
    min_value=2020,
    max_value=2030,
    value=2022
)

month = st.number_input(
    "Month",
    min_value=1,
    max_value=12,
    value=1
)

day = st.number_input(
    "Day",
    min_value=1,
    max_value=31,
    value=1
)

weekday = st.number_input(
    "Weekday",
    min_value=0,
    max_value=6,
    value=5
)


# =========================
# Create input dataframe
# =========================

input_data = pd.DataFrame({
    "Price": [price],
    "Discount": [discount],
    "Inventory Level": [inventory_level],
    "Promotion": [promotion],
    "Competitor Pricing": [competitor_pricing],
    "Category": [category],
    "Region": [region],
    "Weather Condition": [weather],
    "Seasonality": [seasonality],
    "Epidemic": [epidemic],
    "Year": [year],
    "Month": [month],
    "Day": [day],
    "Weekday": [weekday]
})


# =========================
# Prediction
# =========================

st.divider()

if st.button("Predict Demand"):

    prediction = model.predict(input_data)[0]

    prediction = max(0, prediction)

    st.success(
        f"Predicted Demand: {prediction:.0f} Units"
    )