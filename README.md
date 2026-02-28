# ☀️ GridSync: Solar ML Forecaster

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20GUI-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458.svg)


## Overview
GridSync is an interactive machine learning dashboard designed to forecast renewable energy generation. By analyzing meteorological parameters in real-time, the predictive engine calculates the expected Megawatt Hour (MWh) yield of solar grid infrastructure.
Built as a specialized predictive module for broader sustainability ecosystems.


## 🧠 The Tech Architecture

Unlike static calculators, GridSync utilizes a dynamic **Linear Regression** model trained on simulated annual weather patterns. 
* **Inputs:** Cloud Cover Percentage, UV Index, and Ambient Temperature (°C).
* **Processing:** The model maps these non-linear environmental factors to estimate grid efficiency and energy output.
* **Frontend:** Deployed via `Streamlit` for a highly responsive, zero-latency user interface.

  
## 🚀 How to Run the GUI

This project features a live, interactive web dashboard. You do not need to run this in a terminal—it renders a full UI in your browser.
**1. Clone the repository & install dependencies**
```bash
git clone https://github.com/Metamorpho-1/GridSync-Solar-Forecaster.git
cd GridSync-Solar-Forecaster
pip install streamlit pandas numpy scikit-learn
```
**2. Launch the Engine**
```bash
streamlit run app.py
```
*Note: The Streamlit server will automatically open http://localhost:8501 in your default web browser.*
