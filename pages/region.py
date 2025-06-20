import streamlit as st
import pandas as pd

# Dummy data
data = pd.DataFrame({
    "Region": ["North", "South", "East", "West", "North"],
    "Category": ["Electronics", "Furniture", "Electronics", "Furniture", "Electronics"],
    "Sales": [5000, 3000, 4000, 3500, 2500],
    "Discount": [10, 5, 8, 6, 7],
    "Quantity": [50, 30, 40, 35, 25],
    "Profit": [1500, 800, 1200, 1000, 700],
    "Order Date": pd.date_range(start='2023-01-01', periods=5, freq='M')
})

# Title
st.markdown("<h1 style='text-align: center; font-weight: bold;'>Region Level Dashboard</h1>", unsafe_allow_html=True)

# Dropdowns
col1, col2 = st.columns(2)
with col1:
    selected_region = st.selectbox("Region", sorted(data["Region"].unique()))
with col2:
    selected_category = st.selectbox("Category", sorted(data["Category"].unique()))

# Filter data
filtered = data[(data["Region"] == selected_region) & (data["Category"] == selected_category)]

# Metrics
if not filtered.empty:
    total_sales = filtered["Sales"].sum()
    avg_discount = filtered["Discount"].mean()
    total_quantity = filtered["Quantity"].sum()
    total_profit = filtered["Profit"].sum()

    # Display metrics in columns
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Sales", f"₹{total_sales}")
    m2.metric("Average Discount", f"{avg_discount}%")
    m3.metric("Total Quantity", f"{total_quantity}")
    m4.metric("Total Profit", f"₹{total_profit}")
else:
    st.warning("No data found for this selection.")

st.markdown("---")

# Section titles like in image
colA, colB = st.columns(2)
with colA:
    st.subheader("Sales by order date")
    st.subheader("Discounts by order date")
with colB:
    st.subheader("Units by order date")
    st.subheader("Profits by order date")