import plotly.express as px

def plot_churn_risk(df):
    fig = px.histogram(df, x="Churn_Risk", nbins=20, title="Churn Risk Distribution",
                       color_discrete_sequence=['#FF4B4B'])
    return fig\n