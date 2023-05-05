import mysql.connector

class Database:
    def __init__(self):
        # Connect to database
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="paper_trading"
        )
        self.cursor = self.connection.cursor()

    def get_balance(self):
        # Get user's balance from database
        self.cursor.execute("SELECT balance FROM users WHERE id = 1")
        balance = self.cursor.fetchone()[0]
        return balance

    def update_balance(self, balance):
        # Update user's balance in database
        self.cursor.execute("UPDATE users SET balance = %s WHERE id = 1", (balance,))
        self.connection.commit()

    def get_quantity(self, symbol):
        # Get user's quantity of a stock from database
        self.cursor.execute("SELECT SUM(quantity) FROM transactions WHERE user_id = 1 AND symbol = %s", (symbol,))
        quantity = self.cursor.fetchone()[0]
        return quantity if quantity else 0

    def update_transaction(self, symbol, action, quantity, price):
        # Insert a new transaction into database
        self.cursor.execute("INSERT INTO transactions (user_id, symbol, action, quantity, price) VALUES (1, %s, %s, %s, %s)", (symbol, action, quantity, price))
        self.connection.commit()

    def close_connection(self):
        # Close database connection
        self.connection.close()
