import json
import stock_check

ticker = "aapl"
price = str(stock_check.get_current_price(ticker))
ticker_and_price = {'stocks': [{ticker: price}]}
json_ticker_price_data = json.dumps(ticker_and_price, indent=2)
print(json_ticker_price_data)
