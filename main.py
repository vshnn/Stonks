import sys
from trader import Trader
from database import Database
from welcome import display_stonks

# Initialize trader and database objects
trader = Trader()
database = Database()

# Display programm's name
#display_stonks()

while True:
    # Display user menu
    print("\n==== MENU ====")
    print("1. Check balance")
    print("2. Compare stocks")
    print("3. Buy stocks")
    print("4. Sell stocks")
    print("5. Exit")
    
    # Get user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        # Check balance
        balance = trader.check_balance()
        print(f"Your balance is ${balance}")

    elif choice == "2":
        # Compare stocks
        stocks = input("Enter the stocks you want to compare (comma separated): ")
        trader.compare_stocks(stocks)

    elif choice == "3":
        # Buy stocks
        symbol = input("Enter the stock symbol you want to buy: ")
        quantity = int(input("Enter the quantity you want to buy: "))
        trader.buy_stock(symbol, quantity)

    elif choice == "4":
        # Sell stocks
        symbol = input("Enter the stock symbol you want to sell: ")
        quantity = int(input("Enter the quantity you want to sell: "))
        trader.sell_stock(symbol, quantity)

    elif choice == "5":
        # Exit
        print("\n==== THANK YOU ====")
        break

    else:
        print("Invalid choice. Please try again.")


# Close database connection
database.close_connection()
sys.exit()