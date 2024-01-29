import sqlite3
from sqlalchemy import column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base


#
# connection = sqlite3.connect("marketplace.db")
#
# cursor = connection.cursor()
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT NOT NULL,
#     email TEXT NOT NULL,
#     password TEXT NOT NULL
#     facultate integer not null
#     );
#     """
# )


# CONCEPTUALIZARE PRIN INTERMEDIUL OOP
class Users(Base):
    __tablename__ = "users"
    id = Column(Integer)
    username = Column(String(50))
    email = Column(String(50))
    password = Column(String(50))

    #FUNCTIONALITATI BY DEFAULT PRIN

    def all(self):
        pass

c = Users()
c.username



# session.query(Users).all()



# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS facultati(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nume_facultate TEXT NOT NULL,
#     );
#     """
# )
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS products(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     category TEXT NOT NULL,
#     price TEXT NOT NULL,
#     stock_count INTEGER DEFAULT 1,
#     description TEXT
#     );
#     """
# )
#
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS orders(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     customer_id INTEGER NOT NULL,
#     order_date TEXT,
#     FOREIGN KEY (customer_id) REFERENCES users(id)
#     );
#     """
# )
# username = ""
# email = ""
# password = ""
#
# user_sql = f"""
# INSERT INTO users (username, email, password, ...)
# VALUES ({username}, {email}, {password}, ...);
#
# """
# cursor.execute(user_sql)