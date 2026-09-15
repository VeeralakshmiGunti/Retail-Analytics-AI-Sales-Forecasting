
import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt

# ------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------

st.set_page_config(
    page_title="Retail Sales AI Dashboard",
    page_icon="📊",
    layout="wide"
)

# ------------------------------------------
# LOAD DATA
# ------------------------------------------

with open("/content/dashboard_data.pkl", "rb") as f:
    data = pickle.load(f)

# ------------------------------------------
# TITLE
# ------------------------------------------

st.title("📊 Retail Sales AI Dashboard")
st.markdown(
    "### Data-driven analysis, store segmentation and revenue forecasting"
)

st.divider()

# ------------------------------------------
# KPI SECTION
# ------------------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Revenue",
    f"₹{data['overall_revenue']:,.0f}"
)

col2.metric(
    "Units Sold",
    f"{data['total_units']:,}"
)

col3.metric(
    "Transactions",
    f"{data['total_transactions']:,}"
)

st.divider()

# ------------------------------------------
# MONTHLY REVENUE
# ------------------------------------------

st.header("📈 Revenue Trend")

monthly = data["monthly_revenue"].copy()

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(
    monthly["Year_Month"],
    monthly["Revenue"],
    marker="o"
)

ax.set_xlabel("Month")
ax.set_ylabel("Revenue")
ax.set_title("Monthly Revenue Trend")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ------------------------------------------
# CATEGORY PERFORMANCE
# ------------------------------------------

st.header("🏷️ Product Category Performance")

category = data["category_performance"].copy()

st.dataframe(
    category,
    use_container_width=True
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.bar(
    category["Product_Category"],
    category["Revenue"]
)

ax.set_title("Revenue by Product Category")
ax.set_xlabel("Product Category")
ax.set_ylabel("Revenue")

plt.xticks(rotation=30)
plt.tight_layout()

st.pyplot(fig)

# ------------------------------------------
# STORE PERFORMANCE
# ------------------------------------------

st.header("🏪 Store Performance")

stores = data["store_performance"].copy()

st.dataframe(
    stores,
    use_container_width=True
)

# ------------------------------------------
# STORE SEGMENTATION
# ------------------------------------------

st.header("🔎 Store Segmentation")

clusters = data["cluster_assignments"].copy()

st.dataframe(
    clusters,
    use_container_width=True
)

# ------------------------------------------
# CUSTOMER ANALYSIS
# ------------------------------------------

st.header("👥 Customer Contribution")

customers = data["customer_contribution"].copy()

st.dataframe(
    customers,
    use_container_width=True
)

# ------------------------------------------
# PROMOTION ANALYSIS
# ------------------------------------------

st.header("🎯 Promotion Impact")

promotions = data["promotion_impact"].copy()

st.dataframe(
    promotions,
    use_container_width=True
)

# ------------------------------------------
# HOLIDAY ANALYSIS
# ------------------------------------------

st.header("📅 Holiday Impact")

holidays = data["holiday_impact"].copy()

st.dataframe(
    holidays,
    use_container_width=True
)

# ------------------------------------------
# FUTURE FORECAST
# ------------------------------------------

st.header("🔮 Revenue Forecast")

forecast = data["future_forecast"].copy()

st.dataframe(
    forecast,
    use_container_width=True
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    forecast["Year_Month"],
    forecast["Forecast_Revenue"],
    marker="o",
    linestyle="--"
)

ax.set_title("January–June 2025 Revenue Forecast")
ax.set_xlabel("Month")
ax.set_ylabel("Forecast Revenue")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# ------------------------------------------
# AI BUSINESS RECOMMENDATIONS
# ------------------------------------------

st.header("🤖 AI-Powered Business Recommendations")

recommendations = [
    "Prioritize inventory availability for Electronics, the highest-revenue category.",
    "Strengthen customer retention because Returning customers contribute 59.90% of total revenue.",
    "Study STR_103 (Delhi) to identify practices associated with stronger store performance.",
    "Investigate STR_106 (Hyderabad) for product mix, inventory and local demand factors.",
    "Evaluate promotions using transaction volume, units sold, margins and incremental revenue.",
    "Optimize holiday campaigns using relevant products and customer segments.",
    "Use the revenue forecast for inventory, staffing, purchasing and sales planning."
]

for recommendation in recommendations:
    st.write("• " + recommendation)

st.divider()

st.caption(
    "Retail Sales AI Dashboard | Major Project"
)
