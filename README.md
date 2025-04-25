# 🌍 Smart Community Hub

This is a modular, AI-powered infrastructure hub for underserved communities. It simulates real-world edge computing systems using local-only machine learning agents. These agents detect leaks, optimize usage, and provide access to digital literacy tools, even in offline environments.

## Active Modules

# 💧 Leak Detection Agent
- Simulates 48 hours of hourly water usage data (including a leak period)
- Detects abnormal usage with Isolation Forest
- Visualized in an interactive Streamlit dashboard
- Designed to run offline on future edge devices (e.g. Raspberry Pi)

# 🔋 Energy Usage Forecaster Agent
- Simulates 48 hours of electricity usage
- Uses a 6-hour moving average to forecast upcoming energy spikes
- Flags “high-risk” usage periods (e.g., above 350 Wh)
- Ready for future live streaming or Node-RED integration

# 📶 Wi-Fi Load Balancer Agent
- Simulates 48 hours of bandwidth usage across 3 community Wi-Fi access points
- Detects when any point exceeds 60 Mbps and redistributes 10 Mbps to the least-used point
- Produces two files for before/after analysis of agent effectiveness:
  - `simulated_wifi_usage_raw.csv`
  - `simulated_wifi_usage_balanced.csv`


# 🧠 Community Data Logger Agent

- Aggregates output from all agents (leak detection, energy forecast, Wi-Fi usage)
- Produces a unified `hub_log.csv` for system-level analysis and dashboard integration
- Adds timestamp, agent source, and value for each entry
- Prepares your Smart Community Hub for centralized monitoring or real-time simulation

# 📊 Unified Dashboard

A Streamlit-powered interface that brings together all community agents in one place:

- 💧 Leak Detection: Visualizes abnormal water usage
- 🔋 Energy Forecasting: Predicts high energy periods
- 📶 Wi-Fi Load Balancer: Shows bandwidth distribution across access points
- 🧠 System Log: Aggregates recent agent activity

To run the dashboard:

```bash
streamlit run smart_hub_dashboard.py



## 📂 Project Structure



## 📦 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run agents/leak_detection/leak_detection_dashboard.py
