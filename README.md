# 🌍 Smart Community Hub

This is a modular, AI-powered infrastructure hub for underserved communities. It simulates real-world edge computing systems using local-only machine learning agents. These agents detect leaks, optimize usage, and provide access to digital literacy tools, even in offline environments.

## ✅ Active Modules

### 💧 Leak Detection Agent
- Uses Isolation Forest to detect abnormal water usage
- Visualized via Streamlit dashboard
- Fully simulated using synthetic data

## 📦 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run agents/leak_detection/leak_detection_dashboard.py
