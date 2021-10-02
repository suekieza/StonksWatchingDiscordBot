from yahoo_fin import stock_info as si

def get_ticker(ticker=None):
  if not ticker:
    raise ('Not a valid Ticker')
  return ticker

def get_current_price(get_ticker):
    price = si.get_live_price(get_ticker)
    print(price)



