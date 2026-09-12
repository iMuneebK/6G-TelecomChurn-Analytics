import streamlit as st
import pandas as pd
from data_generator import generate_6g_data
from visualizer import plot_churn_risk

st.set_page_config(page_title="6G Churn Predictor", layout="wide")
st.title("🔮 6G Telecom Customer Churn Prediction")
st.markdown("Leveraging AI to analyze next-generation telecom metrics (Terahertz band, Holographic Usage) for churn prediction.")

if st.button("Generate Synthetic 6G Data & Analyze"):
    with st.spinner("Generating data and running inference..."):
        df = generate_6g_data(100)
        # Mocking prediction for dashboard
        df['Churn_Risk'] = df['holographic_usage_hrs'] * -0.05 + df['terahertz_signal_drops'] * 0.1 + 0.2
        df['Churn_Risk'] = df['Churn_Risk'].clip(0, 1)

        st.success("Analysis Complete!")

        col1, col2 = st.columns(2)
        with col1:
            st.dataframe(df[['customer_id', 'terahertz_signal_drops', 'holographic_usage_hrs', 'Churn_Risk']].head(10))
        with col2:
            st.plotly_chart(plot_churn_risk(df), use_container_width=True)\n