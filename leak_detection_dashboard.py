
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title='Smart Hub: Leak Detection', layout='centered')

# --- Title ---
st.title("💧 Smart Community Hub: Leak Detection Agent")

# --- Load Data ---
@st.cache_data
def load_data():
    # Simulate the water usage again for demo purposes
    hours = pd.date_range(start=pd.Timestamp.now().floor('H'), periods=48, freq='H')
    usage = list(np.random.randint(120, 300, size=30)) + list(np.random.randint(600, 800, size=10)) + list(np.random.randint(120, 300, size=8))
    df = pd.DataFrame({'timestamp': hours, 'water_usage_lph': usage})
    return df

df = load_data()

# --- Anomaly Detection ---
model = IsolationForest(contamination=0.2, random_state=42)
df['anomaly'] = model.fit_predict(df[['water_usage_lph']])
df['is_leak'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)

# --- Chart ---
st.subheader("📊 Water Usage Over Time")

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(df['timestamp'], df['water_usage_lph'], label='Water Usage (L/hr)', color='blue')
ax.scatter(df[df['is_leak'] == 1]['timestamp'], df[df['is_leak'] == 1]['water_usage_lph'], color='red', label='Detected Leak')
ax.set_xlabel("Time")
ax.set_ylabel("Liters Per Hour")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# --- Table ---
st.subheader("🔍 Anomaly Table")
st.dataframe(df[df['is_leak'] == 1][['timestamp', 'water_usage_lph']])
