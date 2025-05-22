# 🛍️ Data Driven Customer Segmentation For Targeted Marketring Strategies.

This project uses unsupervised machine learning techniques to segment customers based on their behavior and spending habits. The dataset used is the popular **Mall Customers** dataset. By clustering customers into distinct groups, businesses can better understand and target their customer base.

## 📊 Overview

- **Dataset:** Mall_Customers.csv
- **Techniques Used:** K-Means Clustering, Data Preprocessing, EDA, Visualization
- **Goal:** Group customers into segments based on annual income and spending score

## 🔧 Tools & Libraries Used

- Python
- Pandas
- NumPy
- Seaborn
- Matplotlib
- Scikit-learn

## 📌 Key Steps

1. **Data Cleaning:**
   - Checked for missing and duplicate values
   - Removed irrelevant columns like `CustomerID`
   - Encoded categorical features

2. **Exploratory Data Analysis (EDA):**
   - Visualized correlations using heatmaps
   - Scatter plot of income vs. spending score

3. **Data Normalization:**
   - Used `MinMaxScaler` for normalization

4. **K-Means Clustering:**
   - Elbow method to determine optimal number of clusters
   - Finalized K = 5
   - Segmented data based on `Annual Income` and `Spending Score`

5. **Visualization:**
   - Cluster visualization with distinct colors
   - Centroids plotted for each cluster

## 🔍 Cluster Insights

- **Cluster 1 (Brown):** Low income, high spending → Suggest economical luxury items
- **Cluster 2 (Red):** Low income, low spending → Less likely to convert
- **Cluster 3 (Black):** Medium income and spending → Moderate potential
- **Cluster 4 (Green):** High income, high spending → Prime target group
- **Cluster 5 (Yellow):** High income, low spending → Upselling opportunity

## 📈 Results

- Created 5 distinct customer segments
- Each segment displays unique spending behaviors
- Helps businesses tailor strategies for each group
