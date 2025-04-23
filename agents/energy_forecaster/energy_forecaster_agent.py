
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# --- Simulate 48 hours of hourly energy usage (watts/hour) ---
def simulate_energy_data():
    hours = pd.date_range(start=datetime.now().replace(minute=0, second=0, microsecond=0), periods=48, freq='H')
    usage = []

    for i in range(36):
        usage.append(np.random.randint(150, 300))  # baseline usage
    for i in range(6):
        usage.append(np.random.randint(400, 600))  # peak usage
    for i in range(6):
        usage.append(np.random.randint(150, 300))  # return to normal

    df = pd.DataFrame({'timestamp': hours, 'energy_usage_wh': usage})
    return df

# --- Forecast using 6-hour moving average ---
def forecast_energy_usage(df):
    df['forecast'] = df['energy_usage_wh'].rolling(window=6).mean().shift(1)
    df['high_risk'] = df['forecast'] > 350
    return df.dropna(subset=['forecast'])

# --- Plot actual vs forecast with risk flags ---
def plot_forecast(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['energy_usage_wh'], label='Actual Usage', color='blue')
    plt.plot(df['timestamp'], df['forecast'], label='Forecast (6hr Moving Avg)', color='orange', linestyle='--')

    high_risk_df = df[df['high_risk']]
    plt.scatter(high_risk_df['timestamp'], high_risk_df['forecast'], color='red', label='High Risk Forecast')

    plt.xlabel("Time")
    plt.ylabel("Energy Usage (Wh)")
    plt.title("Energy Usage Forecast with High Risk Flags")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

# --- Main Execution ---
if __name__ == "__main__":
    df = simulate_energy_data()
    df = forecast_energy_usage(df)
    print(df[['timestamp', 'energy_usage_wh', 'forecast', 'high_risk']].tail(10))
    plot_forecast(df)
