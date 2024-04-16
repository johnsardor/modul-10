
import sqlite3


db_connect = sqlite3.connect("TeleBot.sqlite3")

db_cursor = db_connect.cursor()

db_cursor.execute("CREATE TABLE  IF NOT EXISTS users (id INTEGER PRIMARY Key,firstname REAL,lastname REAL)")

# db_cursor.execute("INSERT INTO users  (firstname, lastname) VALUES ('Bunyod','Ergashov')")
# db_connect.execute("""
# CREATE TABLE  IF NOT EXISTS
#
#
# """)
db_cursor.execute("CREATE TABLE  IF NOT EXISTS product (id INTEGER PRIMARY Key,title REAL,price REAL)")
db_cursor.execute("INSERT INTO product  (title, price) VALUES ('Akula Mers','250.000$')")
db_cursor.execute("CREATE TABLE  IF NOT EXISTS orders (id INTEGER PRIMARY Key,product_id REAL,users_id REAL)")
db_cursor.execute("INSERT INTO orders  (product_id,users_id)VALUES ('1','3')")
db_connect.commit()
db_cursor.close()
import sqlite3

db_connect = sqlite3.connect("d13.sqlite3")

db_cursor = db_connect.cursor()


def create_table_users():
    db_cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS users (
    
    id INTEGER PRIMARY KEY, full_name TEXT, phone TEXT, telegram_id INTEGER
    
    )
    """)


def create_table_product():
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY,
        title TEXT,
        price REAL)
    """)



async def insert_user(full_name, phone, telegram_id):
    db_cursor.execute("""
        INSERT INTO users (full_name, phone, telegram_id)
        VALUES(?, ?, ?)""", (full_name, phone, telegram_id))
    db_connect.commit()


# def alter_users():
#     # db_cursor.execute("""
#     # ALTER TABLE users ADD COLUMN age INTEGER DEFAULT 10""")
#     db_cursor.execute("""
#     ALTER TABLE users RENAME first_name to ism""")


def insert_product(title, price):
    db_cursor.execute("""INSERT INTO product (title, price)
    VALUES (?,?)""", (title, price))


def insert_orders(product_id, user_id):
    db_cursor.execute("""INSERT INTO orders (product_id, user_id)
    VALUES (?,?)""", (product_id, user_id))
def read_users():
    db_cursor.execute("""
    SELECT * FROM users""")
    return db_cursor

def create_table_product():
    db_cursor.execute("""
    CREATE TABLE IF NOT EXISTS product(
    id INTEGER PRIMARY KEY,
    title TEXT,
    price REAL,
    phote TEXT)
    """)


async def db_insert_product(title, price, photo):
    db_cursor.execute("""
    INSERT INTO product (title, price, photo)
    VALUES (?,?,?)""",(title, price, photo))
    db_connect.commit()

def get_all_products():
    db_cursor.execute("""
    SELECT * FROM product""")
    return db_cursor.fetchall()
create_table_product()

def db_get_all_products():
    products = db_cursor.execute("""
    SELECT * FROM product""").fetchall()
    return products


db_connect.commit()
# alter_users()
db_connect.close()
