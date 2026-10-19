
def add(a, b):
   #додавання
    return a + b


def subtract(a, b):
    #віднімання
    return a - b


def multiply(a, b):
   #множення
    return a * b


def divide(a, b):
    #ділення
    if b == 0:
        raise ValueError("На нуль ділити не можна!")
    return a / b
