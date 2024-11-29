from time import perf_counter
from functools import wraps

def outer(a, b):
    def inner(x):
        return x ** 2
    print(f"a = {a}, b = {b}")
    return inner
fnc_3 = outer(2, 13)
print(fnc_3(11))

print(fnc_3.__closure__)

def power(n):
    def inner(x):
        return x ** n
    return inner

cube = power(3)
print(cube.__code__.co_freevars)
print(cube(6))

def add(*args):
    """
        doc from add function
    """
    sum = 0
    for el in args:
        sum += el
    return sum

print(add(1, 2 ,5, 7, 18))

def time_it(fnc_name):
    """
        doc from decorator
    """
    @wraps(fnc_name)
    def inner(*args, **kwargs):
        """
            doc from iner function
        """
        start_time = perf_counter()
        result = fnc_name(*args, **kwargs)
        final_time = perf_counter()
        print(f"tim = {final_time - start_time}")
        return result
    return inner

add_executor = time_it(add)

print(add(1, 3))
print(add_executor(4, 6))

def mul(*args):
    prod = 1
    for el in args:
        prod *= el
    return prod
mul_executor = time_it(mul)
print(mul(1, 5, 3, 5))
print(mul_executor(1, 5, 3, 6))

@time_it
def mul(*args):
    """
        doc from multiplay function
    """
    prod = 1
    for el in args:
        prod *= el
    return prod

print(mul(1, 5))

def counter_fnc_calls(fnc):
    count = 0

    @wraps(fnc)
    def inner(*args, **kwargs):
        nonlocal count
        count = count + 1
        result = fnc(*args, **kwargs)
        print(f"Function {fnc.__name__} is called {count} times")
        return result
    return inner


@counter_fnc_calls
def fnc_5():
    print("hallo")

fnc_5()
        