import yfinance as yf
import matplotlib.pyplot as plt
from datetime import date
from database import Database

class Trader:
    todays_date = date.today() 
    def __init__(self):
        # Initialize database object
        self.database = Database()   

    def check_balance(self):
        # Get user's balance from database
        balance = self.database.get_balance()
        return balance

    def compare_stocks(self,ticker):
        ticker1 = ticker.split(',')[0]
        ticker2 = ticker.split(',')[1]
             
        # Extract the prices from the data
        prices1 = yf.download(ticker1,'2020-01-01',self.todays_date)
        prices2 = yf.download(ticker2,'2020-01-01',self.todays_date)

        # Create a plot of the Closing stock prices
        prices1.Close.plot()
        prices2.Close.plot()
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Stock Price Comparison')
        plt.legend([ticker1,ticker2])
        plt.show()

    def buy_stock(self, symbol, quantity):
        # Buy a stock and update user's balance in database
        data = yf.download(symbol,"2020-01-01",self.todays_date, rounding=True)
        price = data['Close'][-1]
        cost = price * quantity
        print(f'Total cost is : {cost:.2f}')
        
        balance = self.database.get_balance()
        if cost > balance:
            print("Insufficient balance.")
        else:
            self.database.update_transaction(symbol, "buy", quantity, price)
            self.database.update_balance(balance - cost)
            print(f"Bought {quantity} shares of {symbol} for ${cost:.2f}")

    def sell_stock(self, symbol, quantity):
        # Sell a stock and update user's balance in database
        data = yf.download(symbol,"2020-01-01",self.todays_date, rounding=True)
        price = data['Close'][-1]
        balance = self.database.get_balance()
        if quantity > self.database.get_quantity(symbol):
            print("Insufficient shares.")
        else:
            self.database.update_transaction(symbol, "sell", quantity, price)
            self.database.update_balance(balance + price * quantity)
            print(f"Sold {quantity} shares of {symbol} for ${price * quantity:.2f}")

            

