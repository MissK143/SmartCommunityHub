import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

st.set_page_config(page_title='Smart Community Hub – Live', layout='wide')
st.title('🌍 Smart Community Hub – Live Dashboard')

# Initialize session state
if 'last_update' not in st.session_state:
    st.session_state.last_update = datetime.now()

# Simulate new data every 10 seconds
def simulate_data():
    now = datetime.now()
    if (now - st.session_state.last_update).total_seconds() > 10:
        # Leak detection simulation
        if 'leak_data' not in st.session_state:
            st.session_state.leak_data = pd.DataFrame(columns=['timestamp', 'water_usage_lph'])
        water_usage = np.random.normal(250, 50)
        if random.random() < 0.05:  # 5% chance of leak
            water_usage += 300
        new_leak = pd.DataFrame({'timestamp': [now], 'water_usage_lph': [max(water_usage, 0)]})
        st.session_state.leak_data = pd.concat([st.session_state.leak_data, new_leak]).tail(50)

        # Energy forecasting simulation
        if 'energy_data' not in st.session_state:
            st.session_state.energy_data = pd.DataFrame(columns=['timestamp', 'energy_usage_wh'])
        energy_usage = np.random.normal(200, 80)
        new_energy = pd.DataFrame({'timestamp': [now], 'energy_usage_wh': [max(energy_usage, 0)]})
        st.session_state.energy_data = pd.concat([st.session_state.energy_data, new_energy]).tail(50)

        # Wi-Fi load balancing simulation
        if 'wifi_data' not in st.session_state:
            st.session_state.wifi_data = pd.DataFrame(columns=['timestamp', 'access_point_1', 'access_point_2', 'access_point_3'])
        ap1 = np.random.randint(10, 100)
        ap2 = np.random.randint(10, 100)
        ap3 = np.random.randint(10, 100)
        new_wifi = pd.DataFrame({'timestamp': [now], 'access_point_1': [ap1], 'access_point_2': [ap2], 'access_point_3': [ap3]})
        st.session_state.wifi_data = pd.concat([st.session_state.wifi_data, new_wifi]).tail(50)

        # Digital literacy simulation
        if 'digital_data' not in st.session_state:
            st.session_state.digital_data = pd.DataFrame(columns=['timestamp', 'user_id', 'category', 'duration_minutes'])
        categories = ['Social Media', 'Gaming', 'Education', 'Entertainment', 'Browsing']
        new_digital = pd.DataFrame({
            'timestamp': [now],
            'user_id': [f"user_{np.random.randint(1,6)}"],
            'category': [random.choice(categories)],
            'duration_minutes': [np.random.randint(5, 30)]
        })
        st.session_state.digital_data = pd.concat([st.session_state.digital_data, new_digital]).tail(100)

        st.session_state.last_update = now

simulate_data()

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💧 Leak Detection",
    "🔋 Energy Forecasting",
    "📶 Wi-Fi Load Balancing",
    "📘 Digital Literacy",
    "🧠 System Log"
])

# Leak Detection Tab
with tab1:
    st.header("💧 Leak Detection Agent (Simulated)")
    if 'leak_data' in st.session_state:
        df = st.session_state.leak_data.set_index('timestamp')
        st.line_chart(df['water_usage_lph'])
    else:
        st.info("Waiting for data...")

# Energy Forecasting Tab
with tab2:
    st.header("🔋 Energy Forecasting Agent (Simulated)")
    if 'energy_data' in st.session_state:
        df = st.session_state.energy_data.copy()
        df['forecast'] = df['energy_usage_wh'].rolling(window=6).mean().shift(1)
        df = df.dropna().set_index('timestamp')
        st.line_chart(df[['energy_usage_wh', 'forecast']])
    else:
        st.info("Waiting for data...")

# Wi-Fi Load Balancing Tab
with tab3:
    st.header("📶 Wi-Fi Load Balancer Agent (Simulated)")
    if 'wifi_data' in st.session_state:
        df = st.session_state.wifi_data.set_index('timestamp')
        st.line_chart(df[['access_point_1', 'access_point_2', 'access_point_3']])
    else:
        st.info("Waiting for data...")

# Digital Literacy Tab
with tab4:
    st.header("📘 Digital Literacy Agent (Simulated)")
    if 'digital_data' in st.session_state:
        df = st.session_state.digital_data.copy()
        usage_summary = df.groupby(['user_id', 'category'])['duration_minutes'].sum().reset_index()
        pivot = usage_summary.pivot(index='user_id', columns='category', values='duration_minutes').fillna(0)
        pivot['Total'] = pivot.sum(axis=1)
        pivot['Education_Ratio'] = pivot['Education'] / pivot['Total']
        pivot['Low_Literacy_Flag'] = pivot['Education_Ratio'] < 0.2

        st.subheader("User Literacy Summary")
        st.dataframe(pivot)

        st.subheader("📊 Education Ratio by User")
        st.bar_chart(pivot['Education_Ratio'])

        flagged = pivot[pivot['Low_Literacy_Flag']]
        if not flagged.empty:
            st.warning("🚨 Users with low digital literacy detected:")
            st.dataframe(flagged[['Education_Ratio']])
        else:
            st.success("✅ All users maintaining healthy digital literacy ratios.")
    else:
        st.info("Waiting for data...")

# System Log Tab
with tab5:
    st.header("🧠 System Log (Static for Now)")
    st.info("Log tab will be upgraded for real-time integration soon.")

# Auto-refresh the page every 10 seconds
st.markdown("""<meta http-equiv="refresh" content="10">""", unsafe_allow_html=True)
