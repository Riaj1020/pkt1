# signal_generator.py
import yfinance as yf
import talib as ta
import pandas as pd

def generate_signal(pair):
    df = yf.download(pair, period="1d", interval="1m")
    df['RSI'] = ta.RSI(df['Close'], timeperiod=14)
    if df['RSI'].iloc[-1] > 70:
        return "Sell Signal"
    elif df['RSI'].iloc[-1] < 30:
        return "Buy Signal"
    else:
        return "No Signal"
