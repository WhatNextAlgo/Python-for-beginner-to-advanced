"""
Decorators belong most probably to the most beautiful and most powerful design possibilities in Python, 
but at the same time the concept is considered by many as complicated to get into. 
To be precise, the usage of decorators is very easy, but writing decorators can be complicated, 
especially if you are not experienced with decorators and some functional programming concepts.

Even though it is the same underlying concept, we have two different kinds of decorators in Python:

Function decorators
Class decorators
"""
#First Steps to Decorators

def succ(x):
    return x + 1
successor = succ
print(successor(10))

del succ
print(successor(5))

#Functions inside Functions
def f():
    
    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
        
    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

f()

def temperature(x):
    def celsiusToFahrenheit(x):
        return (float(9/5) * x + 32)
    
    result = "It's " + str(celsiusToFahrenheit(x))+ " degrees!"
    return result

print(temperature(20))

def factorial(n):
    """ calculates the factorial of n, if n is either a non negative
    integer or a float number x being equivalent to an integer, like
    4.0, 12.0, 8. i.e. no decimals following the decimal point """

    def inner_factorial(x):
        if x == 0:
            return 1
        else:
            return x * inner_factorial(x - 1)
    
    if not isinstance(n,(int,float)):
        raise ValueError("Value is neither an integer nor a float equivalent to int")
    
    if isinstance(n, (int)) and n < 0:
        raise ValueError('Should be a positive integer or 0')
    elif isinstance(n, (float)) and not n.is_integer():
        raise ValueError('value is a float but not equivalent to an int')
        
    else:
        return inner_factorial(n)
    
print(factorial(10))
# factorial(-10) # raise exception : TypeError: n should be a positive int or 0

values = [0, 1, 5, 7.0, -4, 7.3, "7"]
for value in values:
    try: 
        print(value, end=", ")
        print(factorial(value))
    except ValueError as e:
        print(e)


"""
Functions as Parameters
If you solely look at the previous examples, this doesn't seem to be very useful. 
It gets useful in combination with two further powerful possibilities of Python functions. 
Due to the fact that every parameter of a function is a reference to an object and functions 
are objects as well, we can pass functions - or better "references to functions" - as 
parameters to a function. 
We will demonstrate this in the next simple example
"""

def g():
    print("Hi, it's me g")
    print("Thanks for calling me")

def f(func):
    print("Hi, it's me f")
    print("I will call 'func' now")
    func()
    print("func's real name is " + func.__name__)

f(g)

import math
from typing import Any

def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1,2,2.5]:
        res += func(x)
    return res

print(foo(math.sin))
print(foo(math.cos))

"""
Functions returning Functions
The output of a function is also a reference to an object. 
Therefore functions can return references to function objects.
"""

def f(x):
    def g(y):
        return y + x + 3
    return g

print(f(5)(5))

def greeting_func_gen(lang):
    def customized_greeting(name):
        if lang == "de":   # German
            phrase = "Guten Morgen "
        elif lang == "fr": # French
            phrase = "Bonjour "
        elif lang == "it": # Italian
            phrase = "Buongiorno "
        elif lang == "tr": # Turkish
            phrase = "Günaydın "
        elif lang == "gr": # Greek
            phrase = "Καλημερα "
        else:
            phrase = "Hi "
        return phrase + name + "!"
    return customized_greeting

print(greeting_func_gen("tr")("Gülay"))


"""
A more Usefull Example
It is getting more useful and at the same time more mathematically oriented in the following example. 
Let's aussume we have to define many polynomials of degree 2. It may look like this:
"""
def p1(x):
    return 2*x**2 - 3*x + 0.5

def p2(x):
    return 2.3*x**2 + 2.9*x - 20

def p3(x):
    return -2.3*x**2 + 4.9*x - 9

def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x**2 + b * x + c
    return polynomial
    
p1 = polynomial_creator(2, -3, 0.5)
p2 = polynomial_creator(2.3, 2.9, -20)
p3 = polynomial_creator(-2.3, 4.9, -9)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x))


def polynomial_creator(*coefficients):
    """ coefficients are in the form a_n, ... a_1, a_0 
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients[::-1]):
            res += coeff * x** index
        return res
    return polynomial
  
p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(1, 8, -1, 0, 3, 2)
p4 = polynomial_creator(-1, 2, 1)
p5 = polynomial_creator(4, 5, 7, 7, 9, 12, 3, 43, 9)


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x), p5(x))


#A Simple Decorator

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling "+ func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with "+ str(x))

print("we call foo before decoration:")
foo("Hi")

print("We now decorate foo with f:")
foo = our_decorator(foo) 
print("We call foo after decoration:")
foo(42)
print("")

@our_decorator
def bar(x):
    print("Hi, foo has been called with "+ str(x))

bar(45)

print()

@our_decorator
def succ(n):
    return n + 1

#Using Multiple Decorators
def deco1(func):
    
    print('deco1 has been called')
    def helper(x):
        print('helper of deco1 has been called!')
        print(x)
        return func(x) + 3
    return helper
    
def deco2(func):
    
    print('deco2 has been called')
    def helper(x):
        print('helper of deco2 has been called!')
        print(x)
        return func(x) + 2
    return helper
    
def deco3(func):
    
    print('deco3 has been called')
    def helper(x):
        print('helper of deco3 has been called!')
        print(x)
        return func(x) + 1
    return helper
    
@deco3
@deco2
@deco1
def foobar(x):
    return 42

print(foobar(42))

#Usecases for Decorators

def validate_prime(func):
    def helper(x):
        if type(x) == int and x > 0:
            return func(x)
        else:
            raise ValueError("Argument is not an integer")
    return helper

@validate_prime
def is_prime(n):
    return all( n % i for i in range(2,n))

for i in range(1,10):
    print(i, is_prime(i))

try:
    print(is_prime(-1))
except ValueError:
    print("Argument is not a positve integer!")


#Counting Function Calls with Decorators

def call_counter(func):
    def helper(*args,**kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

@call_counter
def mul1(x, y=1):
    return x*y + 1

print(succ.calls)
for i in range(10):
    succ(i)
mul1(3, 4)
mul1(4)
mul1(y=3, x=2)
    
print(succ.calls)
print(mul1.calls)

#Decorators with Parameters
def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        return func(x)
    return function_wrapper

@evening_greeting
def foo(x):
    print(42)

foo("Hi")


def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print("----------------------------------------")
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
            print("----------------------------------------")
        return function_wrapper
    return greeting_decorator

@greeting("καλημερα")
def foo(x):
    print(42)

def bar(x):
    print(42)

foo("Hi")

greeting2 = greeting("καλημερα")
bar = greeting2(bar)
bar("Hi")

def greeting3(func):
    def function_wrapper(x):
        """ function_wrapper of greeting """
        print("Hi, " + func.__name__ + " returns:")
        return func(x)
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__
    return function_wrapper 
@greeting3
def f(x):
    """ just some silly function """
    return x + 4

f(10)
print("function name: " + f.__name__)
print("docstring: " + f.__doc__)
print("module name: " + f.__module__) 

#Classes instead of Functions

class A:
    def __init__(self):
        print("An instance of A was initialized")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("Arguments are ",args,kwds)


x = A()
print("now calling the instance:")
x(3, 4, x=11, y=10)
print("Let's call it again:")
x(3, 4, x=11, y=10)


class Fibonacci:

    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")

class decorator2:
    
    def __init__(self, f):
        self.f = f
        
    def __call__(self):
        print("Decorating", self.f.__name__)
        self.f()

@decorator2
def foo():
    print("inside foo()")

foo()    