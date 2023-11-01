import sqlite3

cx = sqlite3.connect('example.db')

products = [
    {'name': 'Apple', 'price': 10},
    {'name': 'Orange', 'price': 20},
    {'name': 'Banana', 'price': 30},
]

cx.execute('CREATE TABLE products (name text, price real)')

for p in products:
    cx.execute('INSERT INTO products VALUES (:name, :price)', p)
    # or
    # cx.execute('INSERT INTO products VALUES (?, ?)', tuple(p.values()))

cx.commit()

rows = cx.execute('SELECT * FROM products')

for row in rows:
    print(row)

cx.close()
