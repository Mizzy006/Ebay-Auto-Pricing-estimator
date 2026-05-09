# 🚗 Predictive Auto Pricing & Market Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=Tableau&logoColor=white)

## Executive Summary
The secondary automotive market is highly volatile, making it difficult for dealerships and consumers to establish standardized pricing. This project delivers an end-to-end data pipeline that cleans historical listing data, proves market trends statistically, and deploys a production-grade **Random Forest machine learning engine (88.1% Accuracy)** to predict real-time vehicle values.

**Live Application:** https://ebay-auto-pricing-estimator-4qsmqx5fqg9hxgwxb7rzgk.streamlit.app/ 

---

## 🛠️ Data Engineering
Real-world data is notoriously messy. To ensure the machine learning model was trained on reality rather than "data entry garbage," a rigorous, multi-step cleaning pipeline was established.

### 1. Structural Cleaning & Localization
* **String to Numeric Conversion:** Extracted pure integers from string-heavy columns (e.g., converting `"150,000 km"` to `150000` and `"$5,500"` to `5500`).
* **Localization:** Translated raw German market categorizations (e.g., *kleinwagen*, *kombi*, *manuell*) to standard English for global stakeholder readability and model standardization.
* **Missing Value Handling:** Addressed null values logically before moving to algorithmic imputation.

### 2. Multivariate Anomaly Detection
* Utilized an **Isolation Forest Algorithm** to detect and remove **649 multivariate anomalies**. By analyzing the complex interaction between Price, Age, and Odometer, the algorithm successfully isolated and dropped listings that defied actual market trends (e.g., a standard 15-year-old economy car listed for $85,000 due to a user typo).
* **Final Dataset:** A pristine, statistically sound dataset of **32,566 verified listings**.

<img width="1517" height="405" alt="image" src="https://github.com/user-attachments/assets/f7ccc60d-1e48-4c95-935c-f9fc05357b3b" />


## 📊 Market Insights (EDA)

### 1. The Primary Drivers of Depreciation
Correlation analysis revealed the core mathematical drivers of the secondary market:
* **Vehicle Age (-0.80):** The dominant, primary driver of price depreciation.
* **Mileage (-0.46):** A moderate, secondary factor heavily dependent on the vehicle type.

<img width="1098" height="724" alt="image" src="https://github.com/user-attachments/assets/fde45b28-239c-4c01-827f-673ba2ed160c" />


### 2. Brand Value Retention Leaderboard
Not all brands depreciate equally. A median-price cohort analysis revealed:
* **The Niche Premium:** Compacts (Smart, Mini) and enthusiast vehicles (Porsche) hold onto ~20-25% of their original value over a 15-year lifecycle.
* **The Luxury Cliff:** Traditional luxury giants (BMW, Audi, Mercedes) experience sharp initial drops, retaining less than 10.5% of their value due to perceived high secondary-market maintenance costs.

<img width="544" height="718" alt="image" src="https://github.com/user-attachments/assets/62fc6b8b-14f4-4b38-9aaa-42a18e68e4db" />


### 3. The Mileage Sensitivity Matrix
A targeted heatmap proved that wear-and-tear impacts vehicle types differently:
* **High Resilience:** Utility vehicles (SUVs) retain significant value even past 100,000 km.
* **High Fragility:** Sports cars (Coupes, Convertibles) lose over half their value once heavily driven.

<img width="707" height="245" alt="image" src="https://github.com/user-attachments/assets/0647e3dc-48b3-47bc-8ed3-391e0e606034" />


## 💡 Actionable Business Recommendations
Translating data into strategy, this analysis yields three direct recommendations for auto-retail stakeholders:

1. **Inventory Sourcing Strategy:** Dealerships should aggressively source high-mileage SUVs over high-mileage Coupes/Sedans, as SUVs maintain robust profit margins late into their lifecycle.
2. **Purchasing Optimization:** Consumers and corporate fleets seeking luxury vehicles (BMW/Audi) should strictly buy on the secondary market *after* Year 4 to entirely bypass the "Luxury Cliff" depreciation hit.
3. **Appraisal Automation:** Dealerships can utilize the deployed predictive engine to instantly standardize trade-in offers, reducing appraisal time and eliminating human bias.


## 🤖 The Predictive Engine
To handle the multicollinearity between Age and Mileage, a non-linear tree-based ensemble model was deployed.

### Feature Engineering
Model accuracy heavily relied on providing the algorithm with crucial context:
* **Power (PS):** Separated base models from high-performance, high-value luxury trims.
* **Unrepaired Damage:** Acted as a massive penalty multiplier, instantly slashing predicted market value.
* **Gearbox:** Captured the modern market's significant price premium for automatic transmissions.

### Model Performance & Regularization
* **Algorithm:** Random Forest Regressor
* **R-Squared:** `0.881` (Captures 88.1% of complex market variance)
* **Mean Absolute Error (MAE):** `$1,321` (Highly reliable prediction margin for professional appraisal)
* **Optimization:** Applied strict depth limits (`max_depth=20`) and leaf-node constraints (`min_samples_leaf=2`) to compress the model size from 166MB to a web-friendly **13MB**, simultaneously preventing overfitting.

<img width="1652" height="708" alt="image" src="https://github.com/user-attachments/assets/ff80c3e6-2daa-4ba2-8a51-8bea4cda24d7" />



## 🚀 Deployment & Usage

### 1. Real-Time Pricing Estimator
The static Python model was transformed into a dynamic, interactive web application using Streamlit. Stakeholders can input specific vehicle configurations and instantly receive a highly accurate, market-validated price estimate alongside a simulated depreciation curve.

<img width="1919" height="869" alt="image" src="https://github.com/user-attachments/assets/a086c954-98af-4362-8d3d-1c30847f8c6d" />


### 2. Running the App Locally
To run the Streamlit dashboard on your local machine:
```bash
# Clone the repository
git clone [https://github.com/your-username/auto-pricing-estimator.git](https://github.com/your-username/auto-pricing-estimator.git)

# Navigate to the directory
cd auto-pricing-estimator

# Install the required dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
