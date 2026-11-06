
import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Microsoft (MSFT) 5-Year Sharpe Ratio")

data = yf.Ticker("MSFT").history(period="5y")

if not data.empty:
    # Calculate daily returns
    daily_returns = data['Close'].pct_change().dropna()

    # Annual risk-free rate
    risk_free_rate = 0.04

    # Calculate annualized Sharpe Ratio
    sharpe_ratio = (
        (daily_returns.mean() - risk_free_rate / 252)
        / daily_returns.std()
    ) * (252 ** 0.5)

    # Display the result
    st.metric(
        label="5-Year Annualized Sharpe Ratio",
        value=f"{sharpe_ratio:.2f}"
    )

else:
    st.error("No data found for MSFT.")
