import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_data():
    # We use 'data/...' because we will run streamlit from the root folder
    paths = {
        'Ethiopia': 'data/ethiopia_clean.csv', 
        'Kenya': 'data/kenya_clean.csv',
        'Sudan': 'data/sudan_clean.csv', 
        'Nigeria': 'data/nigeria_clean.csv',
        'Tanzania': 'data/tanzania_clean.csv'
    }
    
    dfs = []
    for country, path in paths.items():
        if os.path.exists(path):
            temp_df = pd.read_csv(path)
            temp_df['Country'] = country
            dfs.append(temp_df)
        else:
            # This will show you exactly where it is looking if it fails
            st.error(f"File not found: {os.path.abspath(path)}")
            
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()