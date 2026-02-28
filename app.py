import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# --- UI Setup ---
st.set_page_config(page_title="GridSync Solar ML", page_icon="☀️")
st.title("☀️ GridSync Forecaster")
st.write("Adjust meteorological parameters to predict Megawatt Hour (MWh) yield.")

# --- ML Engine ---
@st.cache_resource
def load_model():
    np.random.seed(101)
    days = 365
    clouds = np.random.uniform(0, 100, days)
    uv = np.random.uniform(0, 10, days)
    temp = np.random.normal(28, 7, days)
    
    yield_mwh = np.maximum((uv * 12) - (clouds * 0.4) - (abs(temp - 25) * 0.1) + np.random.normal(0, 3, days), 0)
    
    df = pd.DataFrame({'clouds': clouds, 'uv': uv, 'temp': temp, 'yield': yield_mwh})
    model = LinearRegression()
    model.fit(df[['clouds', 'uv', 'temp']], df['yield'])
    return model

model = load_model()

# --- Interactive Sliders ---
col1, col2, col3 = st.columns(3)
with col1:
    input_clouds = st.slider("☁️ Cloud Cover (%)", 0, 100, 20)
with col2:
    input_uv = st.slider("☀️ UV Index", 0.0, 11.0, 8.5)
with col3:
    input_temp = st.slider("🌡️ Temp (°C)", -10, 50, 26)

# --- Live Prediction ---
pred_yield = model.predict(pd.DataFrame({'clouds': [input_clouds], 'uv': [input_uv], 'temp': [input_temp]}))[0]

st.divider()
st.metric(label="Predicted Grid Yield", value=f"{max(0, pred_yield):.2f} MWh")
