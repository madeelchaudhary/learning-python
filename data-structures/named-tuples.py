# Named tuples are basically easy-to-create, lightweight object types. Named tuple instances can be referenced using object-like variable dereferencing or the standard tuple syntax. They can be used similarly to struct or other common record types, except that they are immutable.

from collections import namedtuple

# A simple class
Color = namedtuple('Color', 'red green blue')

color = Color(55, 155, 255)
print(color.red)
print(color.green)
print(color.blue)

r, g, b = color
print(r, g, b)

# A more complex class
Person = namedtuple('Person', ['name', 'age', 'country'])

person = Person(name='John Doe', age=30, country='USA')
print(person.name)
print(person.age)
print(person.country)
