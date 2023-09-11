history = []


def push(x):
    history.append(x)


def pop():
    if len(history) > 0:
        return history.pop()
    else:
        return None


def peek():
    if len(history) > 0:
        return history[-1]
    else:
        return None


def is_empty():
    return len(history) == 0


def size():
    return len(history)


def clear():
    history.clear()
