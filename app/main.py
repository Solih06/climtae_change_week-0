import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Climate Dashboard", layout="wide")
st.title("🌍 Africa Climate Comparison")

# Load Data
@st.cache_data
def load_data():
    paths = {
        'Ethiopia': 'data/ethiopia_clean.csv', 'Kenya': 'data/kenya_clean.csv',
        'Sudan': 'data/sudan_clean.csv', 'Nigeria': 'data/nigeria_clean.csv',
        'Tanzania': 'data/tanzania_clean.csv'
    }
    dfs = []
    for country, path in paths.items():
        temp_df = pd.read_csv(path)
        temp_df['Country'] = country
        dfs.append(temp_df)
    return pd.concat(dfs)

df = load_data()

# Sidebar Widgets
st.sidebar.header("Filters")
countries = st.sidebar.multiselect("Select Countries", df['Country'].unique(), default=df['Country'].unique())
year_range = st.sidebar.slider("Year Range", int(df['YEAR'].min()), int(df['YEAR'].max()), (2015, 2026))

# Filter Data
mask = (df['Country'].isin(countries)) & (df['YEAR'].between(year_range[0], year_range[1]))
filtered_df = df[mask]

# Dashboard Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Temp Trends")
    fig_temp = px.line(filtered_df, x='YEAR', y='T2M', color='Country', markers=True)
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    st.subheader("Rainfall Variance")
    fig_rain = px.box(filtered_df, x='Country', y='PRECTOTCORR', color='Country')
    st.plotly_chart(fig_rain, use_container_width=True)

st.write("### Data Overview", filtered_df.groupby('Country')[['T2M', 'PRECTOTCORR']].mean())