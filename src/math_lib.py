import sys

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def prod(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        sys.exit(1)
