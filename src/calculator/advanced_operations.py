
import math


def power(a, b):
   #степінь
    return math.pow(a, b)


def root(a):
  #кв корінь
    if a < 0:
        raise ValueError("Не можна знайти корінь від від'ємного числа!")
    return math.sqrt(a)


def percentage(a, b):
  #відсоток
    return a * b / 100
