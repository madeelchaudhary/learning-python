# Scope
# In Python, we have two types of scope:
# 1. Global scope or module scope
# 2. Local scope or function scope

# Global scope
username = "john"
usermail = "john@example.com"  # Global scope

# Local scope
# Local scope is created whenever a function is called.


def new_user():
    username = "jane"
    usermail = "jane@example.com"  # Local scope
    print(username, usermail)


new_user()
print(username, usermail)

# In Python, we can access variables defined outside the current scope, but we can't modify them.
# If we try to modify them, we'll create a new local variable instead.

# In the following example, we have a global variable x and a function f() that tries to modify it.

x = 5


def f():
    x = 10
    print(x)


f()
print(x)


# To modify a global variable inside a function, we use the global keyword.

x = 5


def f2():
    global x
    x = 10
    print(x)


f2()
