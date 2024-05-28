import yfinance as yf

# printing the end of day stock prices and PE ratio
tickers = ['MSFT','AAPL','META','GOOG']
total = 0
for ticker in tickers:
    ticker_yahoo = yf.Ticker(ticker)
    data = ticker_yahoo.history()
    last_quote = data['Close'].iloc[-1]
    print((ticker, round(last_quote, 2)))
    datainfo = ticker_yahoo.info
    pe_ratio = datainfo['trailingPE']
    print("Price over Earnings ratio:", round(pe_ratio, 2))
    total += pe_ratio
averagePE = total/len(tickers)

# gather the income statement information specific to Diluted EPS
incomeSTMT = yf.Ticker("GOOG").financials.loc['Diluted EPS']

# Check if the "Diluted EPS" entry exists in the income statement
if not incomeSTMT.empty:
    latest_diluted_eps = incomeSTMT.iloc[0]  
    print("Latest Diluted EPS for GOOG:", latest_diluted_eps)
else:
    print("Diluted EPS data not available for GOOG.")
    
# calculating the expected share price from the information gathered, PE ratio times EPS
marketGivenSP = latest_diluted_eps * averagePE

print("The suggested share price for GOOG:", round(marketGivenSP, 2))



    


    



         
     
            


