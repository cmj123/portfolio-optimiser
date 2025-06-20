import yfinance as yf 
import numpy as np 
import scipy.optimize as sc
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import plotly.express as px 
from scipy.stats import norm 

class PortfolioOptimiser:

    def __init__(
            self, stocks, start, end, optimisation_criterion, riskFreeRate=0.045):
        self.stocks = [stock for stock in stocks]
        self.start = start
        self.end = end
        self.optimisation_criterion = optimisation_criterion
        self.riskFreeRate =  riskFreeRate
        self.meanReturns, self.covMatrix = self.getData()
        self.benchmark = self.benchmarkReturns()
        (
            self.optimized_returns,
            self.optimized_std,
            self.optimized_allocation,
            self.efficientList,
            self.targetReturns,
        ) = self.calculatedResults()
        
        st.write([self.optimized_returns,
            self.optimized_std,
            self.optimized_allocation,
            self.efficientList,
            self.targetReturns])

    def optimisation_function(self, constraintSet=(0,1)):

        numAssets = len(self.meanReturns)
        
        constraints = {
            "type": "eq",
            "fun": lambda x: np.sum(x) - 1,
        }
        bound = constraintSet
        bounds = tuple(bound for asset in range(numAssets))

        if self.optimisation_criterion == "Maximize Sharpe Ratio":
            return sc.minimize(
                self.sharpe,
                numAssets * [1.0 / numAssets],
                method="SLSQP",
                bounds=bounds,
                constraints=constraints
            )
        
    def calculatedResults(self):
        optimised_portfolio = (self.optimisation_function())
    
    def benchmarkReturns(self):
        try:
            benchmark_data = yf.download("^GSPC", self.start, self.end)
        except:
            raise ValueError("Unable to download data, try again later!")
        benchmark_returns = benchmark_data["Close"].pct_change().dropna()
        return benchmark_returns
    
    def basicMetrics(self):
        if not all(s.isupper() for s in self.stocks):
            raise ValueError("Enter ticker names in Capital Letters!")
        if len(self.stocks) <=1:
            raise ValueError("More than 1 ticker input required!")
        try:
            stockData = yf.download(self.stocks, start=self.start, end=self.end)
        except:
            raise ValueError("Unable to download data, try again later!")
        stockData = stockData["Close"]

        if len(stockData.columns) != len(self.stocks):
            raise ValueError("Unable to download data for one or more tickers")
        
        returns = stockData.pct_change()
        stdIndividual = returns.std()
      
        return returns, stdIndividual

    def getData(self):

        returns, stdIndividual = self.basicMetrics()
        meanReturns = (returns.mean())
        covMatrix = (returns.cov())

        return meanReturns, covMatrix
