import pandas as pd
import numpy as np

def generate_6g_data(n_samples=1000):
    np.random.seed(42)
    return pd.DataFrame({
        'customer_id': range(1, n_samples + 1),
        'call_duration_mins': np.random.exponential(100, n_samples),
        'data_usage_tb': np.random.uniform(0.1, 5.0, n_samples),
        'terahertz_signal_drops': np.random.poisson(2, n_samples),
        'holographic_usage_hrs': np.random.normal(10, 3, n_samples).clip(0),
        'ai_native_network_score': np.random.uniform(0.5, 1.0, n_samples),
        'churn': np.random.choice([0, 1], p=[0.8, 0.2], size=n_samples)
    })\n