# 🧠 RFM-Based Customer Segmentation using K-Means

## 📌 Project Overview

This project performs **Customer Segmentation** using the RFM (Recency, Frequency, Monetary) model and K-Means clustering.

The objective is to identify distinct customer groups based on purchasing behavior and derive actionable business insights.

---

## 📊 Dataset Features

The dataset was transformed into RFM format with the following features:

- **Recency** – Number of days since last purchase (Lower is better)
- **Frequency** – Total number of purchases
- **Monetary** – Total amount spent by the customer

---

## ⚙️ Methodology

### 1️⃣ Data Preprocessing
- Removed Customer ID (not used for clustering)
- Applied **StandardScaler**
- No log transformation used (raw scaling gave better separation)

### 2️⃣ Finding Optimal K
- Used **Silhouette Score**
- Best result: **K = 5**
- Silhouette Score ≈ **0.61** (Strong clustering)

### 3️⃣ K-Means Clustering
Applied K-Means clustering with:

### 4️⃣ Visualization
- 3D visualization using Recency, Frequency, Monetary
- PCA used for 2D visualization (for reporting)

---

## 📈 Cluster Distribution

| Cluster | Customers | Percentage |
|----------|------------|------------|
| 0 | 244 | 5.63% |
| 1 | 1058 | 24.41% |
| 2 | 3023 | 69.73% |
| 3 | 4 | 0.09% |
| 4 | 6 | 0.14% |

---

## 💰 Revenue Contribution by Cluster

| Cluster | Total Revenue | Revenue % |
|----------|--------------|-----------|
| 0 | 2,871,872 | 32.5% |
| 1 | 518,585 | 6% |
| 2 | 4,020,827 | 45.5% |
| 3 | 277,652 | 3% |
| 4 | 1,144,851 | 13% |

---

## 🏷️ Customer Segment Interpretation

### 🏆 Cluster 4 – Ultra VIP Customers (0.14%)
- Extremely high spending
- Very active buyers
- Contribute ~13% of total revenue
- **Strategy:** Dedicated account management & premium services

---

### 👑 Cluster 3 – Elite Customers (0.09%)
- Extremely high frequency
- High spending
- **Strategy:** Loyalty rewards & retention focus

---

### 💎 Cluster 0 – High-Value Loyal Customers (5.6%)
- Strong purchase behavior
- Contribute ~32% of total revenue
- **Strategy:** Upselling & cross-selling

---

### 📈 Cluster 2 – Core Customers (69.7%)
- Majority customer base
- Contribute ~45% of revenue
- **Strategy:** Increase engagement & purchase frequency

---

### ⚠️ Cluster 1 – At-Risk / Low-Value Customers (24%)
- High recency (inactive)
- Low spending
- **Strategy:** Reactivation campaigns & discounts

---

## 🔥 Key Business Insights

- A very small percentage (~0.23%) of customers contribute ~16% of total revenue.
- 5.6% high-value customers contribute over 32% of revenue.
- Majority customers (70%) generate steady revenue but have growth potential.
- 24% customers are at risk and require engagement strategies.

This segmentation clearly reflects the **Pareto Principle (80/20 Rule)**.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

## 🚀 Future Improvements

- Deploy interactive dashboard
- Apply hierarchical clustering comparison
- Use CLV (Customer Lifetime Value) modeling
- Build automated marketing strategy recommendations

---

## 📌 Conclusion

Using RFM and K-Means clustering, we successfully identified meaningful customer segments with strong separation (Silhouette Score = 0.61).  

This project demonstrates how unsupervised learning can drive actionable business decisions in marketing and customer relationship management.

---

⭐ If you found this project useful, feel free to star the repository!
