import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title="NVDA Sentiment Dashboard", layout="wide")

st.title(" NVDA Stock Price vs. Social Media Sentiment")
st.markdown("""
This dashboard shows the correlation between **Twitter sentiment** (analyzed via FinBERT) 
and **NVIDIA ($NVDA)** stock price movements during 2025-2026.
""")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('data/nvda_processed_final.csv', index_col=0, parse_dates=True)
    return df

df = load_data()

# Sidebar controls
st.sidebar.header("Settings")
show_sentiment = st.sidebar.checkbox("Show Sentiment Bars", value=True)

# Create Plotly Chart
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add Price Line
fig.add_trace(
    go.Scatter(x=df.index, y=df['price'], name="NVDA Price ($)", line=dict(color="#00ff41", width=2)),
    secondary_y=False,
)

# Add Sentiment Bars
if show_sentiment:
    fig.add_trace(
        go.Bar(x=df.index, y=df['sentiment'], name="Sentiment Score", marker_color="rgba(0, 123, 255, 0.3)"),
        secondary_y=True,
    )

fig.update_layout(
    title_text="Price and Sentiment Over Time",
    template="plotly_dark",
    xaxis_title="Date",
    legend=dict(x=0.01, y=0.99)
)

st.plotly_chart(fig, use_container_width=True)

# Key Metrics
col1, col2 = st.columns(2)
with col1:
    corr = df['price'].corr(df['sentiment'])
    st.metric("Overall Correlation", f"{corr:.3f}")
with col2:
    st.metric("Total Analyzed Days", len(df))