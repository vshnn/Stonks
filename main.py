import sys
from colorama import Fore, Style
from trader import Trader
from database import Database
from welcome import display_stonks

# Initialize trader and database objects
trader = Trader()
database = Database()

# Display program's name
display_stonks()

while True:
    # Display user menu
    print(f"{Fore.MAGENTA}\n==== M E N U ===={Style.RESET_ALL}")
    print(f"{Fore.BLUE}1. Check balance{Style.RESET_ALL}")
    print(f"{Fore.BLUE}2. Compare stocks{Style.RESET_ALL}")
    print(f"{Fore.BLUE}3. Buy stocks{Style.RESET_ALL}")
    print(f"{Fore.BLUE}4. Sell stocks{Style.RESET_ALL}")
    print(f"{Fore.RED}5. Exit{Style.RESET_ALL}")

    # Get user choice
    choice = input("Enter your choice: ")

    if choice == "1":
        # Check balance
        balance = trader.check_balance()
        print(f"Your balance is {Fore.GREEN}${balance}{Style.RESET_ALL}")

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
        print(f"\n{Fore.RED}==== THANK YOU ===={Style.RESET_ALL}")
        break

    else:
        print(f"{Fore.RED}Invalid choice. Please try again.{Style.RESET_ALL}")

# Close database connection
database.close_connection()
sys.exit()
