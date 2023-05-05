from trader import Trader
from database import Database

# Initialize trader and database objects
trader = Trader()
database = Database()

# Get user's initial balance from database
initial_balance = database.get_balance()

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
        break

    else:
        print("Invalid choice. Please try again.")

# Update user's balance in database
database.update_balance(trader.check_balance() - initial_balance)

# Close database connection
database.close_connection()
