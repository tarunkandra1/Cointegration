import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import coint


# Get user input for the ticker symbol
ticker_symbol = input("Pick a stock ticker ")
ticker_symbol2 = input("Pick another stock ticker ")

# Get stock ticker data
stock = yf.Ticker(ticker_symbol)
stock2 = yf.Ticker(ticker_symbol2)

# Get 10 years of monthly data
stock_monthly = stock.history(period="1y", interval="1d")
stock_monthly2 = stock2.history(period="1y", interval="1d")

# Check if data was retrieved successfully
if stock_monthly.empty:
    print(f"No data found for ticker: {ticker_symbol}. Please check the symbol and try again.")
else:
    # Calculate log prices
    stock_monthly['LogPrice'] = np.log(stock_monthly['Close'])
    stock_monthly2['LogPrice'] = np.log(stock_monthly2['Close'])

    # Make sure we're using the same timeframe for both stocks
    common_dates = stock_monthly.index.intersection(stock_monthly2.index)
    
    # Create a combined dataframe with log prices for both stocks
    combined_df = pd.DataFrame(index=common_dates)
    combined_df[f'{ticker_symbol}_LogPrice'] = stock_monthly.loc[common_dates, 'LogPrice']
    combined_df[f'{ticker_symbol2}_LogPrice'] = stock_monthly2.loc[common_dates, 'LogPrice']
    combined_df = combined_df.dropna()
    
    # Perform linear regression
    x = combined_df[f'{ticker_symbol}_LogPrice'].values.reshape(-1, 1)
    y = combined_df[f'{ticker_symbol2}_LogPrice'].values
    
    model = LinearRegression()
    model.fit(x, y)

    # Calculate predicted values
    y_pred = model.predict(x)
    
    # Calculate residuals
    residuals = y - y_pred
    
    # Add residuals to the dataframe
    combined_df['Residuals'] = residuals
    


    # The 5% Critical Value for the Engle-Granger Test for cointegration is -3.33613. We test this statistic using the coint function
    result = coint(y,x)
    print('Test statistic:', result[0])
    print('P-value:', result[1])
    print('Critical values:', result[2])
    if(result[1] < 0.9):
        print("Not cointegrated at a 90% confidence level")
    else:
        print("The stocks are cointegrated at a 90% confidence level")

        #This plots the residual of the prediction of what stock 2 should be based on stock 1. If above 0 short stock 2
        #and long stock 1, if below 0, long stock 2 and short stock 1
        plt.plot(combined_df.index,combined_df['Residuals'])
        plt.show()
        