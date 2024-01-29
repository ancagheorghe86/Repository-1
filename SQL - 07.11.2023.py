import sqlite3

connection = sqlite3.connect("marketplace.db")

cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
    );
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    price TEXT NOT NULL,
    stock_count INTEGER DEFAULT 1,
    description TEXT
    );
    """
)

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS orders(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT,
    FOREIGN KEY (customer_id) REFERENCES users(id)
    );
    """
)
username = "test"
email = 'test@yahoo.com'
password = "1234"

user_sql = f"""
INSERT INTO users (username, email, password)
VALUES (?, ?, ?
);

"""
cursor.execute(user_sql,(username,email, password))


connection.commit()

connection.close()
