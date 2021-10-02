import json
import stock_check

ticker = "aapl"
stock_check.get_current_price(ticker)
json_data = json.loads(stock_check.get_current_price())
print(json_data)
