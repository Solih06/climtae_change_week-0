Climate Change Analysis: East & West Africa

This project provides a comprehensive analysis of climate trends across Ethiopia, Kenya, Sudan, Nigeria, and Tanzania to support policy development for COP32. It features a data-driven approach to identifying regional climate vulnerabilities and an interactive dashboard for real-time exploration.

 **Key Features**

Multi-Country Comparison: Integrated climate data across 5 African nations to identify regional risks.

Statistical Insights: Confirmed regional variance using One-Way ANOVA and Z-score anomaly detection.

Interactive Dashboard: Built with Streamlit to visualize temperature trends and rainfall volatility dynamically.

**Project Structure**

app/: Contains the Streamlit dashboard (main.py) and modular helper functions (utils.py).

notebooks/: Jupyter notebooks covering EDA, data cleaning, and statistical testing.

data/: Cleaned CSV datasets for each country.

scripts/: Python utility scripts for data processing and directory initialization.

**Setup & Installation**

Follow these steps to set up the project on your local machine:

Clone the repository:

git clone [https://github.com/Solih06/climate_change_week-0.git](https://github.com/Solih06/climate_change_week-0.git)
cd climate_change_week-0


Install dependencies:

pip install -r requirements.txt


Run the Dashboard:

streamlit run app/main.py


**Project Milestones**

1. Exploratory Data Analysis (EDA)

Cleaned NASA Power data by replacing sentinel values (-999) with NaNs.

Performed forward-fill imputation to handle missing time-series data.

Identified seasonal patterns (e.g., Ethiopia's Kiremt rainy season) and extreme weather anomalies.

2. Cross-Country Statistical Analysis

Synthesized data from five nations into a master analysis.

Conducted One-Way ANOVA ($p < 0.001$), identifying Sudan as the most thermally stressed region.

Analyzed rainfall variance to pinpoint flood-risk zones in Nigeria and Tanzania.

3. Interactive Visualization

Developed a Streamlit dashboard allowing users to filter by country and year range.

Integrated Plotly charts to visualize temperature spikes and rainfall distribution.

**Key Findings (COP32 Summary)**

Based on the statistical analysis of climate data from 1990 to 2025, we have identified the following critical trends for the East and West African regions:

* **Thermal Stress in Sudan:** Statistical testing (One-Way ANOVA) confirmed that **Sudan** experiences significantly higher average temperatures compared to its neighbors, with a notable increase in "extreme heat" days over the last decade.
* **Rainfall Volatility in Nigeria & Tanzania:** While average rainfall remains steady, the **variance** has increased. This suggests a transition toward more extreme "wet-dry" cycles, increasing the risk of flash flooding in agricultural zones.
* **Warming Trends in Ethiopia & Kenya:** Both nations show a consistent upward trend in minimum night-time temperatures, which can have a direct impact on crop maturation cycles and local biodiversity.
* **Anomaly Detection:** Z-score analysis identified 2023 and 2024 as "Climate Anomaly Years" across all five countries, characterized by record-breaking temperature spikes that deviate significantly from the 30-year mean.


**Dashboard Preview**

Developed as part of the Climate Change Analysis Challenge (Week 0).
![Climate Dashboard](Screenshot_27-4-2026_103149_localhost.jpeg)
![Climate Dashboard](Screenshot_27-4-2026_9951_localhost.jpeg)
