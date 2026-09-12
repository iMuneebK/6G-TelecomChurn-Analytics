import pandas as pd

def create_features(df):
    df = df.copy()
    df['usage_per_drop'] = df['data_usage_tb'] / (df['terahertz_signal_drops'] + 1)
    df['premium_user'] = (df['holographic_usage_hrs'] > 15).astype(int)
    return df\n