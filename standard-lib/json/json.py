from json import dumps, loads

# convert a Python object to a JSON string
products = [
    {'name': 'Sony Xperia Z5', 'price': 500},
    {'name': 'iPhone 6S', 'price': 600},
    {'name': 'Samsung Galaxy S6', 'price': 400, 'image': None}
]
json_str = dumps(products)


# convert a JSON string to a Python object
products = loads(json_str)
