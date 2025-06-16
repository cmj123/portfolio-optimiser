import datetime as dt
import pandas as pd
import streamlit as st
import plotly.express as px 
import streamlit_shadcn_ui as ui
from PIL import Image
from interpretations import appinfo, optimization_strategies_info


def main():
    im = Image.open("EfficientFrontier.png")

    st.set_page_config(page_title="Portfolio Optimisation Dashboard", page_icon=im)

    st.markdown("## Portfolio Optimisation Dashboard")
    col1, col2 = st.columns([0.14, 0.86], gap="small")
    col1.write("`Created by: `")
    linkedin_url = "https://www.linkedin.com/in/edijemeni/"
    col2.markdown(
        f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="15" height="15" style="vertical-align: middle; margin-right: 10px;">`Esuabom Dijemeni`</a>',
        unsafe_allow_html=True,
    )

    appinfo()

    with st.expander("View Optimisation Strategies"):
        optimization_strategies_info()

if __name__ == "__main__":
    main()