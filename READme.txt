# 💧 Smart Community Hub: Leak Detection Agent

This is a simulated water leak detection module built for a Smart Community Hub platform. It uses synthetic data, anomaly detection (Isolation Forest), and a Streamlit dashboard to flag water usage anomalies — laying the foundation for an edge-deployable AI agent aligned with SDG 11.

## Features
- Simulated water usage data generator
- Anomaly detection using scikit-learn
- Interactive Streamlit dashboard
- Designed to run offline and support real-world sensor inputs in future phases

## How to Run

```bash
pip install pandas numpy matplotlib scikit-learn streamlit
streamlit run leak_detection_dashboard.py
