import streamlit as st
import altair as alt
import pandas as pd
import time
import numpy as np
import os

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

train = pd.read_csv("data/train_data.csv")
train.set_index("Month", inplace=True)
val = pd.read_csv("data/val_data.csv")
val.set_index("Month", inplace=True)
preds = pd.read_csv("data/output_pred.csv")
preds.set_index("Month", inplace=True)

sectors = train.Sector.unique()

select = st.selectbox("Select a sector:",sectors)

t_ = train.query(f"Sector=='{select}'")
v_ = val.query(f"Sector=='{select}'")
p_ = preds.query(f"Sector=='{select}'")
conc = pd.concat([t_,v_,p_], axis=1)[["highMobileGB", "ets_predictions"]]
conc.columns = ["Train", "Validation", "Predictions"]
conc.reset_index(inplace=True)
print(conc)

st.markdown(f"# Plotting {select}")
st.sidebar.header(f"Plotting {select}")
st.write(
    """Only Mobility traffic is taken into consideration for this SC. WHSIA will be implemented later this year. Values are in GB"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
chart = st.line_chart(conc, x="Month")

# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")