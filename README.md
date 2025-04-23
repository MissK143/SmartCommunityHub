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
- Ready to evolve into a real-time load balancing agent for future SDG-aligned smart infrastructure
 
**AI Logic**: Rule-based Redistribution  
**SDG Impact**:  
- ⚙️ SDG 9 – Industry, Innovation, and Infrastructure  
- 🏙️ SDG 11 – Sustainable Cities and Communities


## 📂 Project Structure



## 📦 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run agents/leak_detection/leak_detection_dashboard.py
