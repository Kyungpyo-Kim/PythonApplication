import os
import pybithumb
import time
import datetime

con_key = os.getenv("BITHUMB_CONNECT_KEY")
sec_key = os.getenv("BITHUMB_SECRET_KEY")
bithumb = pybithumb.Bithumb(con_key, sec_key)

DECISION_PREMIUM_RATIO = 0.5


def get_target_price(ticker):
    df = pybithumb.get_ohlcv(ticker)
    yesterday = df.iloc[-2]

    today_open = yesterday['close']
    yesterday_high = yesterday['high']
    yesterday_low = yesterday['low']
    target = today_open + (yesterday_high - yesterday_low) * \
        DECISION_PREMIUM_RATIO
    return target


def buy_crypto_currency(ticker):
    krw = bithumb.get_balance(ticker)[2]
    orderbook = pybithumb.get_orderbook(ticker)
    sell_price = orderbook['asks'][0]['price']
    unit = krw/float(sell_price)
    # bithumb.buy_market_order(ticker, unit)


def get_yesterday_ma5(ticker):
    df = pybithumb.get_ohlcv(ticker)
    close = df['close']
    ma = close.rolling(window=5).mean()
    return ma[-2]

def sell_crypto_currency(ticker):
    unit = bithumb.get_balance(ticker)[0]
    # bithumb.sell_market_order(ticker, unit)


now = datetime.datetime.now()
mid = datetime.datetime(now.year, now.month, now.day) + datetime.timedelta(1)
ma5 = get_yesterday_ma5("BTC")
target_price = get_target_price("BTC")

while True:
    try:
        now = datetime.datetime.now()
        if mid < now < mid + datetime.datetime.delta(seconds=10):
            print("정각입니다")
            target_price = get_target_price("BTC")
            mid = datetime.datetime(now.year, now.month,
                                    now.day) + datetime.timedelta(1)
            sell_crypto_currency("BTC")
            ma5 = get_yesterday_ma5("BTC")

        current_price = pybithumb.get_current_price("BTC")
        print("Current price: {}".format(current_price))
        krw = bithumb.get_balance("BTC")[2]
        print("Current balance {}".format(krw))

        if (current_price > target_price) and (current_price > ma5):
            buy_crypto_currency("BTC")

        print(now, "vs", mid)

    except:
        print("Error")

    time.sleep(1)
