import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === PAGE SETUP ===
st.set_page_config(page_title="Supermarket Sales Dashboard", layout="wide")
st.title("🛒 Supermarket Sales Dashboard")

# === LOAD DATA ===
@st.cache_data
def load_data():
    return pd.read_csv("cleaned_supermarket_sales.csv")

df = load_data()

# Convert 'Date' to datetime (in case it's not)
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
sales_by_product = filtered_df.groupby("Product line")["Sales"].sum().sort_values()

fig1, ax1 = plt.subplots(figsize=(10, 5))
sales_by_product.plot(kind="barh", color="teal", ax=ax1)
ax1.set_xlabel("Sales")
st.pyplot(fig1)

# === MONTHLY SALES TREND ===
st.subheader("📈 Monthly Sales Trend")
filtered_df["Month"] = filtered_df["Date"].dt.to_period("M")
monthly_sales = filtered_df.groupby("Month")["Sales"].sum()

fig2, ax2 = plt.subplots(figsize=(10, 4))
monthly_sales.plot(marker="o", ax=ax2)
ax2.set_ylabel("Sales")
ax2.set_title("Monthly Sales Trend")
st.pyplot(fig2)

# === RATING DISTRIBUTION ===
st.subheader("🎯 Rating Distribution by Customer Type")
fig3, ax3 = plt.subplots()
sns.boxplot(data=filtered_df, x="Customer type", y="Rating", palette="Pastel1", ax=ax3)
st.pyplot(fig3)

# === RAW DATA (Optional) ===
with st.expander("📄 Show Raw Data"):
    st.dataframe(filtered_df)

# === PAYMENT METHOD PIE CHART ===
st.subheader("💳 Payment Method Breakdown")

payment_counts = filtered_df["Payment"].value_counts()

fig4, ax4 = plt.subplots()
ax4.pie(payment_counts, labels=payment_counts.index, autopct="%1.1f%%", startangle=90)
ax4.axis("equal")  # Equal aspect ratio makes pie a circle
st.pyplot(fig4)


# === DOWNLOAD FILTERED DATA ===
csv = filtered_df.to_csv(index=False).encode('utf-8')

st.download_button(
    label="⬇️ Download Filtered Data as CSV",
    data=csv,
    file_name='filtered_supermarket_data.csv',
    mime='text/csv'
)
