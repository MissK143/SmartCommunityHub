
import pandas as pd
import os

# File paths
files = {
    'leak_detector': "simulated_water_usage.csv",
    'energy_forecaster': "simulated_energy_usage.csv",
    'wifi_balancer': "simulated_wifi_usage_raw.csv"
}

logs = []

# --- Leak Detection ---
if os.path.exists(files['leak_detector']):
    df = pd.read_csv(files['leak_detector'])
    df = df[df['is_leak'] == 1].tail(10)
    df['agent'] = 'leak_detector'
    df = df.rename(columns={'water_usage_lph': 'value'})
    logs.append(df[['timestamp', 'value', 'agent']])

# --- Energy Forecasting ---
if os.path.exists(files['energy_forecaster']):
    df = pd.read_csv(files['energy_forecaster'])
    df['forecast'] = df['energy_usage_wh'].rolling(window=6).mean().shift(1)
    df = df.dropna(subset=['forecast']).tail(10)
    df['agent'] = 'energy_forecaster'
    df = df.rename(columns={'forecast': 'value'})
    logs.append(df[['timestamp', 'value', 'agent']])

# --- Wi-Fi Load Balancer ---
if os.path.exists(files['wifi_balancer']):
    df = pd.read_csv(files['wifi_balancer'])
    df['value'] = df[['access_point_1', 'access_point_2', 'access_point_3']].mean(axis=1)
    df = df[['timestamp', 'value']].tail(10)
    df['agent'] = 'wifi_balancer'
    logs.append(df)

# --- Combine Logs ---
if logs:
    hub_log = pd.concat(logs, ignore_index=True)
    hub_log['timestamp'] = pd.to_datetime(hub_log['timestamp'])
    hub_log.to_csv("hub_log.csv", index=False)
    print("✅ Hub log created: hub_log.csv")
else:
    print("⚠️ No agent logs found. Please ensure data files exist.")
