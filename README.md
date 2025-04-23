# 🌍 Smart Community Hub

This is a modular, AI-powered infrastructure hub for underserved communities. It simulates real-world edge computing systems using local-only machine learning agents. These agents detect leaks, optimize usage, and provide access to digital literacy tools, even in offline environments.

## Active Modules

# 💧 Smart Community Hub – Leak Detection Agent

This is a simulated AI-powered water leak detection module developed as part of the **Smart Community Hub** — a modular edge computing platform designed to empower underserved communities with real-time resource monitoring and offline-first intelligence.

This first agent focuses on detecting abnormal water usage patterns, showcasing the power of anomaly detection and local inference even in low-resource environments.

## 🔍 Features

- Simulates 48 hours of hourly water usage data (including a leak period)
- Detects abnormal usage with Isolation Forest
- Visualized in an interactive Streamlit dashboard
- Designed to run offline on future edge devices (e.g. Raspberry Pi)

## 📂 Project Structure



## 📦 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run agents/leak_detection/leak_detection_dashboard.py
