import datetime as dt
import pandas as pd
import streamlit as st
import plotly.express as px 
import streamlit_shadcn_ui as ui
from PIL import Image
import time
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

    col1, col2 = st.columns([0.14, 0.86], gap="small")
    col1.write("`Code at: `")
    github_url = "https://github.com/cmj123/portfolio-optimiser"
    col2.markdown(
        f'<a href="{github_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="15" height="15" style="vertical-align: middle; margin-right: 10px;">`Portfolio Optimiser`</a>',
        unsafe_allow_html=True,
    )


    appinfo()

    with st.expander("View Optimisation Strategies"):
        optimization_strategies_info()

    if "stocks" not in st.session_state:
        st.session_state.stocks_list = ["AAPL, TSLA, MSFT, SNOW"]

    default_tickers_str = ", ".join(st.session_state.stocks_list)
    
    cont1 = st.container(border=True)
    cont1.markdown("### Input Parameters")
    stocks = cont1.text_input(
        "Enter Tickers (separated by commas)", value = default_tickers_str
    )
    start, end = cont1.columns(2)
    start_date = start.date_input(
        "Start Date",
        max_value=dt.date.today() - dt.timedelta(days=1),
        min_value=dt.date.today() - dt.timedelta(days=1250),
        value=dt.date.today() - dt.timedelta(days=365)
    )

    end_date = end.date_input(
        "End Date",
        max_value=dt.date.today(),
        min_value=start_date + dt.timedelta(days=1),
        value=dt.date.today(),
    )

    col1, col2 = cont1.columns(2)
    optimisation_criterion = col1.selectbox(
        "Optimisation Objective",
        options=[
            "Maximize Sharpe Ratio",
            "Minimize Volatility",
            "Maximize Sortino Ratio",
            "Minimize Tracking Error",
            "Maximize Information Ratio",
            "Minimize Conditional Value-at-Risk",
        ],
    )

    riskFreeRate_d = col2.number_input(
        "Risk Free Rate (%)",
        min_value=0.00,
        max_value=100.00,
        step=0.001,
        format="%0.3f",
        value=4.432,
        help = "10 Year Bond Yield"
    )

    calc = cont1.button("Calculate")
    riskFreeRate = riskFreeRate_d/100

    st.session_state.stocks_list = [s.strip() for s in stocks.split(",")]
   

    if calc: 
        with st.spinner("Buckle Up! Financial Wizardry in Progress...."):
                time.sleep(3)    
        with st.container(border=True):
            st.markdown('#### Optimised Porfolio Performance - Summary')
            col1, col2 = st.columns(2)
            col1.markdown(f"**Returns**: {46.41}%")
            col1.markdown(f"**Volatility**: {22.75}%")
            col1.markdown(f"**Sharpe Ratio**: {1.74}")
            col1.markdown(f"**Sortino Ratio**: {2.91}")
            col2.markdown(f"**Time Period**: {365} days")

            st.markdown("#### Optimiserd Porfolio Allocation")
            alocCol, pieCol = st.columns(2)
            with alocCol:
                allocations = {
                    'AAPL':28.72,
                    "TSLA": 30.48,
                    "MSFT":20,
                    "SNOW":20.80
                }
                df_allocations = pd.DataFrame(allocations.items(), columns=['Tickers', 'Allocation (%)'])
                ui.table(df_allocations)
            with pieCol:
                fig = px.pie(df_allocations, values='Allocation (%)',names='Tickers')
                fig.update_layout(
                    width=180,
                    height=200,
                    margin=dict(t=20, b=0, l=0, r=0),
                )
                st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()