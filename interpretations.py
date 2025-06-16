import streamlit as st

def appinfo():
    st.markdown("This app optimizes a stock portfolio using a range of optimization techniques to identify the most efficient allocation based on the selected criteria. Simply enter your stock tickers, choose a historical date range, and watch as the app analyzes performance and delivers tailored allocation recommendations to help you achieve your investment goals.")

def optimization_strategies_info():
    st.write("")
    st.markdown("**Sharpe Ratio**: Measures the return per unit of total risk taken. This metric is ideal for investors seeking to maximize returns relative to risk. A higher Sharpe Ratio indicates more effective risk management alongside return generation.")
    st.markdown( "**Volatility**: Represented by the standard deviation of portfolio returns, this metric is crucial for investors focused on reducing fluctuations in their portfolio's value. Lower volatility signifies a more stable investment, aligning with conservative investment strategies.")
    st.markdown("**Sortino Ratio**: This ratio emphasizes downside risk by measuring returns per unit of negative volatility. It’s beneficial for investors who prioritize capital preservation and want to avoid significant losses. A higher Sortino Ratio indicates better performance in adverse market conditions.")
    st.markdown("**Tracking Error**: This metric measures how closely a portfolio's returns follow its benchmark. It’s suitable for investors who want to ensure their portfolio closely aligns with a benchmark index. A lower Tracking Error indicates consistency with benchmark performance.")
    st.markdown("**Information Ratio**: This ratio evaluates returns above a benchmark relative to the active risk taken. It’s ideal for active investors who seek to outperform a benchmark while managing risk. A higher Information Ratio indicates successful active management.")
    st.markdown("**Conditional Value-at-Risk (CVaR)**: This metric estimates potential losses in extreme market conditions, focusing on worst-case scenarios. It's essential for risk-averse investors looking to safeguard their capital against severe downturns. Lower CVaR values indicate better risk protection.")
    st.markdown("*Benchmark: S&P 500")