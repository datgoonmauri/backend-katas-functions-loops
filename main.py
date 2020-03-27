
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    add_num = x + y
    if add_num:
        return add_num
    if add_num == x+(-y):
        return add_num


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if y == 0:
        return 0
    elif y > 0:
        return x + multiply(x, y - 1)
    elif y < 0:
        return -multiply(x, -y)


def power(x, n):
    """Raise x to power n, where n >= 0"""
    if n == 0:
        return 1
    else:
        n % 2 == 0
        return x ** n



def factorial(x):
    fact = 1
    """Compute factorial of x, where x > 0"""
    for i in range(1, x + 1):
        fact = fact * i
    return fact


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    if n < 0:
        print(Error)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    # your code to call functions above
    pass
