import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


symbols = ['GOOG', 'AAPL', 'W', 'TRIP', 'SQ', 'TSLA']
pnls = {i: yf.Ticker(i).history(period="ytd") for i in symbols}

result = {}
for pnl in pnls:
    s = pnls.get(pnl)['Close']
    for key, value in s.iteritems():
        if key.strftime("%Y-%m-%d") in result:
            v = result[key.strftime("%Y-%m-%d")]
            v[pnl] = value
        else:
            result[key.strftime("%Y-%m-%d")] = {pnl: value}

# print(result)

pd.DataFrame(result).T.plot(kind='line')
plt.grid()
plt.show()
