import os
import pybithumb

con_key = os.getenv("BITHUMB_CONNECT_KEY")
sec_key = os.getenv("BITHUMB_SECRET_KEY")

bithumb = pybithumb.Bithumb(con_key, sec_key)

for ticker in pybithumb.get_tickers():
    balance = bithumb.get_balance(ticker)
    if balance[0]:
        print(ticker, format(balance[0], 'f'))

# order = bithumb.buy_limit_order("BTC", 3900000, 0.001)
# print(order)

krw = bithumb.get_balance("BTC")[2]
orderbook = pybithumb.get_orderbook("BTC")
asks = orderbook['asks']
sell_price = asks[0]['price']
unit = krw/sell_price
print(unit)

# order = bithumb.buy_market_order("BTC", unit) # 시장가 매수
# print(order)


# order = bithumb.sell_limit_order("BTC", 4000000, 1)
# print(order)

unit = bithumb.get_balance("BTC")[0]
print(unit)
# order = bithumb.sell_limit_order("BTC", 4000000, unit)
# print(order)

unit = bithumb.get_balance("BTC")[0]
# order = bithumb.sell_limit_order("BTC", 4000100, unit)
# print(order)

unit = bithumb.get_balance("BTC")[0]
# order = bithumb.sell_market_order("BTC", unit) # 시장가 매도
# print(order)

# import time
# 코드 생략 
# order = bithumb.buy_limit_order("BTC", 3000000, 0.001 )
# print(order)

# time.sleep(10)
# cancel = bithumb.cancel_order(order)
# print(cancel)