# Retail Analytics & AI-Powered Sales Forecasting System

**Name:** Veeralakshmi Gunti

## 📌 Project Overview

The **Retail Analytics & AI-Powered Sales Forecasting System** is a data analytics project designed to analyze retail sales data, identify important business patterns, understand store and customer performance, and forecast future revenue.

The project uses **Exploratory Data Analysis, K-Means clustering, ARIMA time-series forecasting, and an interactive Streamlit dashboard** to generate meaningful business insights and support data-driven decision-making.

## 🎯 Objectives

- Analyze sales performance across different stores and product categories.
- Identify revenue trends and monthly sales patterns.
- Analyze customer contribution and purchasing behavior.
- Evaluate the impact of promotions and holidays on revenue.
- Segment stores based on their performance using K-Means clustering.
- Forecast future monthly revenue using ARIMA.
- Generate business insights and recommendations.
- Present the analysis through an interactive dashboard.

## 📊 Dataset

**Dataset Name:** Retail Sales Data

**Data Period:** January 2023 – December 2024

**Number of Records:** 73,000

**Number of Columns:** 19

The dataset contains retail transaction-level information covering stores, products, customers, sales, discounts, promotions, inventory, ratings, regions, and holidays.

### Dataset Features

- Date
- Store_ID
- Store_Location
- Product_ID
- Product_Category
- Product_Subcategory
- Brand
- Unit_Price
- Units_Sold
- Total_Sales
- Discount_Percentage
- Revenue
- Customer_Type
- Payment_Mode
- Promotion_Applied
- Stock_On_Hand
- Store_Rating
- Region
- Holiday_Flag

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Statsmodels
- Streamlit
- Jupyter Notebook

## 🔍 Project Workflow

### 1. Data Loading and Exploratory Data Analysis

The retail dataset was loaded and analyzed to understand its structure and characteristics.

The analysis included:

- Dataset shape and structure
- Data types
- Missing value analysis
- Duplicate record analysis
- Date range analysis
- Store performance
- Product category performance
- Customer contribution
- Promotion analysis
- Holiday analysis
- Revenue trends

### 2. Advanced Exploratory Data Analysis

Additional analysis was performed to identify important business patterns, including:

- Year-over-year revenue analysis
- Monthly revenue trends
- Monthly seasonality
- Regional performance
- Top brands
- Top products
- Discount and revenue analysis
- Promotion effectiveness
- Category performance by year
- Store performance

### 3. Store Segmentation

**K-Means Clustering** was used to segment stores based on their performance and business characteristics.

The clustering analysis considered:

- Total Revenue
- Total Units Sold
- Total Transactions
- Average Discount
- Average Stock
- Average Store Rating

The clustering process included evaluation of suitable cluster groups, followed by store segmentation using K-Means.

The final analysis identified **2 store clusters**.

### 4. Monthly Revenue Analysis

Monthly revenue was calculated for the complete two-year period from January 2023 to December 2024.

The monthly revenue data was divided into:

- Training period: January 2023 – June 2024
- Testing period: July 2024 – December 2024

This monthly time-series data was used for revenue forecasting.

### 5. Revenue Forecasting

The project uses **ARIMA (1,1,1)** for monthly revenue forecasting.

The model was trained using historical monthly revenue and evaluated on the six-month testing period.

### 📈 Forecast Model Evaluation

The ARIMA model achieved the following evaluation results:

- **MAE:** ₹53,533,069.81
- **RMSE:** ₹66,246,112.58
- **MAPE:** **3.02%**

The model was then used to forecast revenue for the next six months:

**January 2025 – June 2025**

The average forecasted monthly revenue is approximately:

**₹1.73 billion**

## 💡 Key Business Insights

### Product Category Performance

**Electronics** is the highest revenue-generating product category, contributing approximately **20.22%** of total revenue.

### Customer Contribution

**Returning customers** contribute approximately **59.90%** of total revenue, highlighting the importance of customer retention.

### Store Performance

**STR_103 (Delhi)** recorded the highest revenue among the stores.

**STR_106 (Hyderabad)** recorded the lowest revenue among the stores.

The difference between the highest and lowest store revenue is approximately **3.62%**.

### Promotion Impact

Promotional transactions generated slightly lower average revenue per transaction compared with non-promotional transactions.

Therefore, promotion effectiveness should be evaluated using additional measures such as transaction volume, units sold, margins, and incremental revenue.

### Holiday Impact

Holiday transactions showed slightly lower average revenue per transaction compared with non-holiday transactions.

This indicates an opportunity to optimize holiday campaigns and product targeting.

### Revenue Forecast

The ARIMA model achieved a **3.02% MAPE** on the testing period and forecasts relatively stable monthly revenue for January–June 2025.

## 🤖 Business Recommendations

- Prioritize inventory availability for high-revenue product categories such as Electronics.
- Strengthen customer retention through loyalty programs and personalized offers.
- Study high-performing stores to identify successful operational practices.
- Investigate lower-performing stores based on product mix, inventory, and customer demand.
- Evaluate promotions using transaction volume, units sold, margins, and incremental revenue.
- Optimize holiday campaigns using relevant products and customer segments.
- Use revenue forecasts for inventory planning, staffing, purchasing, and sales planning.
- Combine store segmentation, customer analysis, and forecasting for better business decision-making.

## 📊 Interactive Streamlit Dashboard

The project includes an interactive **Streamlit dashboard** for visualizing important retail analytics results.

### Dashboard Features

- 📈 Revenue Trend
- 🏷️ Product Category Performance
- 🏪 Store Performance
- 🔎 Store Segmentation
- 👥 Customer Contribution
- 🎯 Promotion Impact
- 📅 Holiday Impact
- 🔮 Revenue Forecast
- 🤖 AI-Powered Business Recommendations

The dashboard provides a single interface for exploring retail performance and forecasting results.

## 📁 Project Structure

```text
Retail-Analytics-AI-Sales-Forecasting/
│
├── Retail_Analytics_AI_Sales_Forecasting.ipynb
├── Retail_Sales_Data_Unlox.csv
├── app.py
├── dashboard_data.pkl
├── requirements.txt
└── README.md
```

## ▶️ How to Run the Project

### Run the Jupyter Notebook

Open the following notebook:

`Retail_Analytics_AI_Sales_Forecasting.ipynb`

The notebook contains the complete data analysis, store segmentation, revenue forecasting, business insights, and dashboard data preparation workflow.

### Run the Streamlit Dashboard

Install the required libraries:

```bash
pip install -r requirements.txt
```
## 📌 Project Outcome

The project successfully transforms raw retail sales data into meaningful business insights using data analysis, visualization, store segmentation, and time-series forecasting.

The system helps to:

- Understand overall retail sales and revenue performance.
- Identify high-performing product categories and stores.
- Analyze customer contribution and purchasing behavior.
- Evaluate the impact of promotions and holidays on revenue.
- Segment stores based on their performance using K-Means clustering.
- Forecast future monthly revenue using ARIMA.
- Support inventory, staffing, purchasing, and sales planning.
- Present key analytics and recommendations through an interactive Streamlit dashboard.

Overall, the project provides a data-driven approach to understanding retail performance and supporting better business decision-making.

## 👩‍💻 Author

**Veeralakshmi Gunti**

B.Tech – Computer Science and Engineering

Anurag Engineering College
