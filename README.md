# 💡 Smart Community Hub – Live AI Dashboard

A real-time, modular edge-AI dashboard built to simulate and monitor smart community infrastructure in underserved areas.

This project showcases live data agents for:
- 💧 Water leak detection
- 🔋 Energy usage forecasting
- 📶 Wi-Fi load balancing
- 📘 Digital literacy behavior tracking

Built using **Python + Streamlit**, this dashboard helps visualize AI-powered insights in support of:
- 🌍 **SDG 9** – Industry, Innovation, and Infrastructure
- 🏙️ **SDG 11** – Sustainable Cities and Communities
- 🎓 **SDG 4** – Quality Education (via Digital Literacy Agent)

---

## 🧠 Agents Overview

| Agent | Description |
|-------|-------------|
| **Leak Detection** | Flags abnormal water usage in real time |
| **Energy Forecast** | Predicts energy spikes using rolling averages |
| **Wi-Fi Load Balancer** | Tracks bandwidth across 3 access points |
| **Digital Literacy** | Evaluates user internet habits and flags low educational use |
| **System Log** | (To be upgraded) Centralized system insight |

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/MissK143/SmartCommunityHub.git
cd SmartCommunityHub

# Install dependencies
pip install -r requirements.txt

# Run simulators in separate terminals:
python leak_stream_simulator.py
python energy_stream_simulator.py
python wifi_stream_simulator.py
python digital_literacy_stream_simulator.py

# Run the dashboard
streamlit run smart_hub_dashboard_local.py
```

## 📚 About This Project Setup

This project was originally designed with **modular architecture**, separating:
- Real-time simulators (data generators)
- Dashboard (data visualization)

This is the **professional** way to build scalable edge-AI systems.

---

## ☁️ Special Note for Deployment

Because platforms like **Streamlit Cloud** allow only a single script to run, a special deployment version of the dashboard was created:
- Simulators are integrated **directly into the dashboard**
- No external terminal processes required

✅ If working **locally**, you can run agents separately for full modularity.  
✅ If **deploying**, use the integrated version for smooth cloud hosting.

---

## 🖥️ Running Locally vs Cloud Deployment

| File Name | Purpose |
|-----------|---------|
| smart_hub_dashboard_local.py | Local development with multiple simulators running manually |
| smart_hub_dashboard_live.py | Streamlit Cloud version with integrated manual simulation button |

When deploying to Streamlit Cloud, use **smart_hub_dashboard_live.py**.
When working locally with separate simulators, use **smart_hub_dashboard_local.py**.

## 🔄 Manual Control Instructions

This Smart Hub dashboard uses manual simulation for real-time data.

- To simulate new water, energy, Wi-Fi, and literacy data, click the **"Simulate New Data"** button in the sidebar.
- This prevents data loss and allows better control over real-time behavior.
- The dashboard does not auto-refresh by itself — user triggers updates manually.

This design improves performance and stability, especially when deployed on Streamlit Cloud.
