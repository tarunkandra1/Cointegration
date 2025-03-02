# Stock Cointegration Analysis  

This Python script analyzes the cointegration of two selected stocks using historical price data from Yahoo Finance. It applies statistical methods, including linear regression and the Engle-Granger cointegration test, to determine if the chosen stocks share a long-term equilibrium relationship.  

## Features  
- Retrieves 10 years of monthly stock price data from Yahoo Finance  
- Calculates log prices for normalization  
- Performs linear regression to model the relationship between the two stocks  
- Computes residuals and tests for cointegration  
- Displays test statistics, p-values, and critical values for interpretation  

## Requirements  
Ensure you have the following Python libraries installed:  
```bash
pip install pandas numpy matplotlib yfinance scikit-learn statsmodels
