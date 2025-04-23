
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# --- Simulate Bandwidth Usage for 3 Access Points ---
def simulate_wifi_data():
    timestamps = pd.date_range(start=datetime.now().replace(minute=0, second=0, microsecond=0), periods=48, freq='H')
    data = {
        'timestamp': timestamps,
        'access_point_1': np.random.randint(20, 70, size=48),
        'access_point_2': np.random.randint(20, 70, size=48),
        'access_point_3': np.random.randint(20, 70, size=48)
    }
    df = pd.DataFrame(data)
    return df

# --- Load Balancing Logic ---
def balance_load(df):
    df_balanced = df.copy()
    
    def redistribute(row):
        max_ap = row[1:].idxmax()
        min_ap = row[1:].idxmin()
        if row[max_ap] > 60:
            row[max_ap] -= 10
            row[min_ap] += 10
        return row
    
    df_balanced.iloc[:, 1:] = df_balanced.iloc[:, 1:].apply(redistribute, axis=1)
    return df_balanced

# --- Main Execution ---
if __name__ == "__main__":
    df_raw = simulate_wifi_data()
    df_balanced = balance_load(df_raw)
    
    df_raw.to_csv("simulated_wifi_usage_raw.csv", index=False)
    df_balanced.to_csv("simulated_wifi_usage_balanced.csv", index=False)
    
    print("Simulation complete. Files saved:")
    print("  - simulated_wifi_usage_raw.csv")
    print("  - simulated_wifi_usage_balanced.csv")
