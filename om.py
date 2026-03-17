def bhegakaro(a, b):
    return a + b

def badkaro(a, b):
    return a - b

def guniyakaro(a, b):
    return a * b

def bhagyakaro(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: cannot divide by zero"