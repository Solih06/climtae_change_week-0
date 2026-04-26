# Climate Challenge - Week 0

## Project Structure
- `src/`: Source code for the project.
- `notebooks/`: Jupyter notebooks for data analysis.
- `scripts/`: Python scripts for data processing.
- `tests/`: Unit tests for the codebase.

## Setup Instructions
To reproduce the development environment:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Solih06/climtae_change_week-0.git](https://github.com/Solih06/climtae_change_week-0.git)
   cd climtae_change_week-0

  ---

## **Interim Progress Report: Climate Change Analysis (Week 0)**

**Date:** April 26, 2026  
**Status:** Tasks 1 & 2 Completed

### **1. Task 1: Project Environment & Infrastructure**
* **Repository Management:** Established a GitHub repository with a clear branching strategy.
* **Folder Hierarchy:** Implemented a standard data science directory structure: `/data`, `/notebooks`, `scripts/`, and `tests/`.
* **Environment Control:** Created `requirements.txt` and `.gitignore` to manage dependencies and keep the repo clean.

### **2. Task 2: Exploratory Data Analysis (EDA) - Ethiopia**
* **Data Cleaning:** Replaced NASA sentinel values (`-999`) with `NaN` and performed forward-fill imputation.
* **Statistical Analysis:** Used Z-score analysis to identify extreme weather anomalies.
* **Visualizations:** Generated a daily temperature line plot and a monthly precipitation bar chart identifying the **Kiremt** rainy season.
* **Output:** Saved the refined data as `data/ethiopia_clean.csv`.

### **3. Technical Challenges**
Resolved "refspec" and branch synchronization errors by aligning local work with the remote `eda-ethiopia` branch before merging into `main`.
