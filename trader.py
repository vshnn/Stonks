import requests
import json
import time
import random
import pandas as pd
import numpy as np
from database import Database

class Trader:
    def __init__(self):
        # Initialize database object
        self.database = Database()

        # Load Yahoo finance API credentials
        with open("credentials.json", "r") as f:
            credentials = json.load(f)
            self.base_url = credentials["base_url"]
            self.headers = {
                "X-RapidAPI-Key": credentials["api_key"]
            }

    def fetch_data(self, symbol):
        # Fetch data from Yahoo finance API
        url = f"{self.base_url}/stock/v2/get-historical-data?symbol={symbol}"
        response = requests.get(url, headers=self.headers)
        data = response.json()["historical"]

        # Convert data to pandas dataframe
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
        df.set_index("date", inplace=True)
        df.sort_index(inplace=True)
        df.drop(columns=["adjClose", "adjHigh", "adjLow", "adjOpen", "adjVolume"], inplace=True)
        df.columns = ["open", "high", "low", "close", "volume"]

        return df

    def check_balance(self):
        # Get user's balance from database
        balance = self.database.get_balance()
        return balance

    def compare_stocks(self, stocks):
        # Compare stocks based on their historical prices
        stocks = stocks.split(",")
        data = {}
        for stock in stocks:
            df = self.fetch_data(stock)
            data[stock] = df["close"]
        df = pd.DataFrame(data)
        returns = np.log(df / df.shift(1))
        print(returns.cumsum().tail())

    def buy_stock(self, symbol, quantity):
        # Buy a stock and update user's balance in database
        df = self.fetch_data(symbol)
        price = df["close"].iloc[-1]
        cost = price * quantity
        balance = self.database.get_balance()
        if cost > balance:
            print("Insufficient balance.")
        else:
            self.database.update_transaction(symbol, "buy", quantity, price)
            self.database.update_balance(balance - cost)
            print(f"Bought {quantity} shares of {symbol} for ${cost:.2f}.")

    def sell_stock(self, symbol, quantity):
        # Sell a stock and update user's balance in database
        df = self.fetch_data(symbol)
        price = df["close"].iloc[-1]
        balance = self.database.get_balance()
        if quantity > self.database.get_quantity(symbol):
            print("Insufficient shares.")
        else:
            self.database.update_transaction(symbol, "sell", quantity, price)
            self.database.update_balance(balance + price * quantity)
            print(f"Sold {quantity} shares of {symbol} for ${price * quantity:.2f}.")

            

