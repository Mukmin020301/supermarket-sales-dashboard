import streamlit as st
import pandas as pd
import plotly.express as px

# === PAGE SETUP ===
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")
st.title("🛒 Supermarket Sales Dashboard")

# === LOAD DATA ===
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_supermarket_sales.csv")

df = load_data()

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# === SIDEBAR FILTERS ===
st.sidebar.header("Filter Data")

selected_city = st.sidebar.multiselect(
    "Select City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

selected_customer = st.sidebar.multiselect(
    "Customer Type:",
    options=df["Customer type"].unique(),
    default=df["Customer type"].unique()
)

selected_product = st.sidebar.multiselect(
    "Product Line:",
    options=df["Product line"].unique(),
    default=df["Product line"].unique()
)

# === APPLY FILTERS ===
filtered_df = df[
    (df["City"].isin(selected_city)) &
    (df["Customer type"].isin(selected_customer)) &
    (df["Product line"].isin(selected_product))
]

# === METRICS ROW ===
total_sales = filtered_df["Sales"].sum()
average_rating = filtered_df["Rating"].mean()
gross_income = filtered_df["gross income"].sum()

col1, col2, col3 = st.columns(3)
col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("⭐ Average Rating", f"{average_rating:.2f}")
col3.metric("💼 Gross Income", f"${gross_income:,.2f}")

# === SALES BY PRODUCT LINE ===
st.subheader("📦 Sales by Product Line")
sales_by_product = filtered_df.groupby("Product line")["Sales"].sum().sort_values().reset_index()

fig1 = px.bar(
    sales_by_product,
    x="Sales",
    y="Product line",
    orientation="h",
    title="Sales by Product Line",
    color="Sales",
    color_continuous_scale="Teal"
)
st.plotly_chart(fig1, use_container_width=True)

# === MONTHLY SALES TREND ===
st.subheader("📈 Monthly Sales Trend")
filtered_df["Month"] = filtered_df["Date"].dt.to_period("M").astype(str)
monthly_sales = filtered_df.groupby("Month")["Sales"].sum().reset_index()

fig2 = px.line(
    monthly_sales,
    x="Month",
    y="Sales",
    markers=True,
    title="Monthly Sales Trend"
)
st.plotly_chart(fig2, use_container_width=True)

# === RATING DISTRIBUTION ===
st.subheader("🎯 Rating Distribution by Customer Type")
fig3 = px.box(
    filtered_df,
    x="Customer type",
    y="Rating",
    color="Customer type",
    title="Customer Rating Distribution"
)
st.plotly_chart(fig3, use_container_width=True)

# === PAYMENT METHOD PIE CHART ===
st.subheader("💳 Payment Method Breakdown")
payment_counts = filtered_df["Payment"].value_counts().reset_index()
payment_counts.columns = ["Payment Method", "Count"]

fig4 = px.pie(
    payment_counts,
    names="Payment Method",
    values="Count",
    title="Payment Method Breakdown"
)
st.plotly_chart(fig4, use_container_width=True)

# === RAW DATA (Optional) ===
with st.expander("📄 Show Raw Data"):
    st.dataframe(filtered_df)

# === DOWNLOAD FILTERED DATA ===
csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_supermarket_data.csv',
    mime='text/csv'
)
