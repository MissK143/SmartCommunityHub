
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title='Smart Community Hub - Live', layout='wide')
st.title('🌍 Smart Community Hub – Live Dashboard')

# Define tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "💧 Leak Detection",
    "🔋 Energy Forecasting",
    "📶 Wi-Fi Load Balancing",
    "📘 Digital Literacy",
    "🧠 System Log"
])

# --- Leak Detection Tab ---
with tab1:
    st.header("💧 Leak Detection Agent (Live)")
    try:
        df = pd.read_csv("leak_stream.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df_recent = df.tail(50)

        fig, ax = plt.subplots()
        ax.plot(df_recent['timestamp'], df_recent['water_usage_lph'], label='Water Usage (L/h)', color='blue')

        leaks = df_recent[df_recent['water_usage_lph'] > 500]
        ax.scatter(leaks['timestamp'], leaks['water_usage_lph'], color='red', label='Leak Detected')

        ax.set_xlabel("Time")
        ax.set_ylabel("Usage (L/h)")
        ax.set_title("Real-Time Water Usage")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Leak stream failed to load: {e}")

# --- Energy Forecasting Tab ---
with tab2:
    st.header("🔋 Energy Forecasting Agent (Live)")
    try:
        df = pd.read_csv("energy_stream.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['forecast'] = df['energy_usage_wh'].rolling(window=6).mean().shift(1)
        df = df.dropna().tail(50)

        fig, ax = plt.subplots()
        ax.plot(df['timestamp'], df['energy_usage_wh'], label='Actual Usage', color='blue')
        ax.plot(df['timestamp'], df['forecast'], label='Forecast', color='orange', linestyle='--')

        high_risk = df[df['forecast'] > 350]
        ax.scatter(high_risk['timestamp'], high_risk['forecast'], color='red', label='High Risk Forecast')

        ax.set_xlabel("Time")
        ax.set_ylabel("Energy (Wh)")
        ax.set_title("Energy Forecast (Live)")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Energy stream failed to load: {e}")

# --- Wi-Fi Load Balancing Tab ---
with tab3:
    st.header("📶 Wi-Fi Load Balancer Agent (Live)")
    try:
        df = pd.read_csv("wifi_stream.csv")
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df_recent = df.tail(50)

        fig, ax = plt.subplots()
        ax.plot(df_recent['timestamp'], df_recent['access_point_1'], label='AP1')
        ax.plot(df_recent['timestamp'], df_recent['access_point_2'], label='AP2')
        ax.plot(df_recent['timestamp'], df_recent['access_point_3'], label='AP3')

        ax.set_xlabel("Time")
        ax.set_ylabel("Bandwidth (Mbps)")
        ax.set_title("Wi-Fi Bandwidth Usage")
        ax.legend()
        ax.grid(True)
        st.pyplot(fig)
    except Exception as e:
        st.warning(f"Wi-Fi stream failed to load: {e}")

# --- Digital Literacy Tab ---
with tab4:
    st.header("📘 Digital Literacy Agent (Live)")
    try:
        df = pd.read_csv("digital_literacy_output.csv")
        df = df.fillna(0)

        st.subheader("User Literacy Summary")
        st.dataframe(df)

        st.subheader("📊 Education Ratio by User")
        fig, ax = plt.subplots()
        ax.bar(df['user_id'], df['Education_Ratio'], color=['red' if flag else 'green' for flag in df['Low_Literacy_Flag']])
        ax.axhline(0.2, color='orange', linestyle='--', label='Minimum Recommended Threshold')
        ax.set_ylabel("Education Time Ratio")
        ax.set_title("Digital Literacy Ratios (Last Hour)")
        ax.legend()
        st.pyplot(fig)

        flagged = df[df['Low_Literacy_Flag']]
        if not flagged.empty:
            st.warning("🚨 The following users are showing signs of low digital literacy:")
            st.write(flagged[['user_id', 'Education_Ratio']])
        else:
            st.success("✅ All users are maintaining healthy digital literacy ratios.")
    except Exception as e:
        st.warning(f"Digital literacy data not available or failed to load: {e}")

# --- System Log Tab ---
with tab5:
    st.header("🧠 System Log (Static for Now)")
    st.info("Log tab will be upgraded for real-time integration soon.")

# Auto-refresh the entire page every 10 seconds
st.markdown("""<meta http-equiv="refresh" content="10">""", unsafe_allow_html=True)
