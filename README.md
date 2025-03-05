# Stock Cointegration Analysis  

This Python script analyzes the cointegration of two selected stocks using historical price data from Yahoo Finance. It applies statistical methods, including linear regression and the Engle-Granger cointegration test, to determine if the chosen stocks share a long-term equilibrium relationship. In the future, I will continue working on this code so it can automatically scan indexes find statistically significant cointegration, and perform statistical arbitrage.

## Features  
- Retrieves monthly stock price data from Yahoo Finance  
- Calculates log prices for normalization  
- Performs linear regression to model the relationship between the two stocks  
- Computes residuals and tests for cointegration  
- Displays test statistics, p-values, and critical values for interpretation  

Here is an example output of regressing MSFT on Apple:
Test statistic: -3.2633338723501963
P-value: 0.05995929898588575
Critical values: [-3.90080167 -3.33856151 -3.04613746]
The stocks are cointegrated at a 90% confidence level
<img width="1198" alt="image" src="https://github.com/user-attachments/assets/a47e6250-eff7-4ffc-af0a-0c89b7fe2dcf" />

## Requirements  
Ensure you have the following Python libraries installed:  
```bash
pip install pandas numpy matplotlib yfinance scikit-learn statsmodels
![Uploading image.png…]()
