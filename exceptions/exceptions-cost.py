from timeit import timeit

exception_block = """
def divide(x, y):
    if y == 0:
        raise ZeroDivisionError('division by zero')
    else:
        return x / y

try:
    divide(10, 0)
except ZeroDivisionError as e:
    # print(e)
    pass
"""

exception_block_time = timeit(stmt=exception_block, number=10000)

print('exception block time:', exception_block_time)

without_exception_block = """
def divide(x, y):
    if y == 0:
        return None
    else:
        return x / y
        
result = divide(10, 0)

if result is None:
    # print('division by zero')
    pass
"""

without_exception_block_time = timeit(
    stmt=without_exception_block, number=10000)

print('without exception block time:', without_exception_block_time)

# exception block time: 0.006939499988220632
# without exception block time: 0.0016502999933436513

# raise exception is slower than if else block
# use exception block only when you need to handle an exception
