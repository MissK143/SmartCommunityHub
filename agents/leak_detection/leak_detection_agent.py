# filepath: c:\Users\kmalu\Downloads\leak_detection_agent.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# --- Generate Simulated Water Usage Data ---
def simulate_water_usage():
    hours = pd.date_range(start=pd.Timestamp.now().floor('H'), periods=48, freq='H')
    usage = []

    # Normal usage
    usage += list(np.random.randint(120, 300, size=30))
    # Leak period
    usage += list(np.random.randint(600, 800, size=10))
    # Back to normal
    usage += list(np.random.randint(120, 300, size=8))

    df = pd.DataFrame({'timestamp': hours, 'water_usage_lph': usage})
    return df

# --- Detect Anomalies ---
def detect_anomalies(df):
    model = IsolationForest(contamination=0.2, random_state=42)
    df['anomaly'] = model.fit_predict(df[['water_usage_lph']])
    df['is_leak'] = df['anomaly'].apply(lambda x: 1 if x == -1 else 0)
    return df

# --- Visualize ---
def plot_results(df):
    plt.figure(figsize=(12, 6))
    plt.plot(df['timestamp'], df['water_usage_lph'], label='Water Usage (L/hr)')
    plt.scatter(df[df['is_leak'] == 1]['timestamp'], df[df['is_leak'] == 1]['water_usage_lph'], color='red', label='Detected Leak')
    plt.xlabel('Timestamp')
    plt.ylabel('Liters Per Hour')
    plt.title('Simulated Water Usage with Leak Detection')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# --- Main Run ---
if __name__ == "__main__":
    df = simulate_water_usage()
    df = detect_anomalies(df)
    print(df[['timestamp', 'water_usage_lph', 'is_leak']])
    plot_results(df)
    df.to_csv("simulated_water_usage.csv", index=False)
