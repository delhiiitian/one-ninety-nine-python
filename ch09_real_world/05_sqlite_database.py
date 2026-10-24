"""9.5 Databases with SQLite.

Real-world comparison: a filing cabinet with an index. A text file is
a pile of papers; a database is a cabinet with labelled drawers
(tables) and a librarian (SQL) who finds exactly the rows you ask
for. SQLite is built into Python, and it powers apps on most phones.
"""

import sqlite3

db = sqlite3.connect(":memory:")       # use a file name like "shop.db" to keep it
db.row_factory = sqlite3.Row           # rows behave like dictionaries

db.execute("""
    CREATE TABLE products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        stock INTEGER DEFAULT 0
    )
""")

items = [("tea", 20, 100), ("coffee", 40, 50), ("samosa", 15, 0), ("juice", 60, 25)]
db.executemany("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", items)
db.commit()

print("All products:")
for row in db.execute("SELECT * FROM products ORDER BY price"):
    print(f"  {row['id']} {row['name']:7} Rs {row['price']:>5} stock {row['stock']}")

# Always use ? placeholders. Never build SQL with f-strings: that
# opens the door to SQL injection attacks.
max_price = 30
cheap = db.execute("SELECT name FROM products WHERE price <= ?", (max_price,)).fetchall()
print("Under Rs 30:", [r["name"] for r in cheap])

db.execute("UPDATE products SET stock = stock + ? WHERE name = ?", (40, "samosa"))
db.execute("DELETE FROM products WHERE name = ?", ("juice",))
db.commit()

total = db.execute("SELECT SUM(price * stock) AS value FROM products").fetchone()
print("Stock value: Rs", total["value"])

out_of_stock = db.execute("SELECT COUNT(*) FROM products WHERE stock = 0").fetchone()[0]
print("Out of stock items:", out_of_stock)
db.close()
