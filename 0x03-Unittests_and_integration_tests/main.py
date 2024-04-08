#!/usr/bin/env python3

#response = requests.get('https://jsonplaceholder.typicode.com/todos/')
"""
import time
from functools import wraps

def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        print(f'key: {key}')
        print(cache)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@memoize
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    start = time.time()
    print(fib(5))
    stop = time.time()
    print(stop - start)
"""

