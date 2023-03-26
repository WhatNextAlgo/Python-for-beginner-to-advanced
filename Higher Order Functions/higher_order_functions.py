#The general syntax of a lambda function is quite simple:
#lambda argument_list: expression

sum = lambda x,y : x + y
print(sum(3,4))

#The map() Function
"""
As we have mentioned earlier, the advantage of the lambda operator can be seen 
when it is used in combination with the map() function. 
map() is a function which takes two arguments:

r = map(func, seq)

The first argument func is the name of a function and the second a sequence 
(e.g. a list) seq. map() applies the function func to all the elements of the sequence seq. 
Before Python3, map() used to return a list, where each element of 
the result list was the result of the function func applied on the corresponding 
element of the list or tuple "seq". With Python 3, map() returns an iterator.

The following example illustrates the way of working of map():
"""
def fahrenheit(T):
    return (float(9)/5) * T + 32

def celsius(T):
    return (float(5)/9) * (T - 32)

temperatures = (36.5, 37, 37.5, 38, 39)
F = list(map(fahrenheit,temperatures))
C = list(map(celsius,F))
print(F)
print(C)

fahrenheit = lambda T : (float(9)/5) * T + 32
celsius = lambda T : (float(5)/9) * (T - 32)

print(list(map(fahrenheit,temperatures)))
print(list(map(celsius,list(map(fahrenheit,temperatures)))))

a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9] 

print(list(map(lambda x,y,z : x + y + z,a,b,c)))
print(list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c)))

#Mapping a List of Functions
from math import sin,cos, tan,pi
def map_functions(x,functions):
    res = []
    for func in functions:
        res.append(func(x))
    return res

def map_func(x,functions):
    return [func(x) for func in functions]
family_of_functions = (sin, cos, tan)
print(map_functions(pi, family_of_functions))
print(map_func(pi, family_of_functions))

#Filtering

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
odd_number = list(filter(lambda x: x % 2,fibonacci))
print(odd_number)
even_number = list(filter(lambda x: x % 2 == 0,fibonacci))
print(even_number)

#Reducing a List
import functools
print(functools.reduce(lambda x,y: x+y, [47,11,42,13]))

from functools import reduce
f = lambda a,b: a if (a > b) else b
print(reduce(f, [47,11,42,102,13]))

orders = [ ["34587", "Learning Python, Mark Lutz", 4, 40.95], 
           ["98762", "Programming Python, Mark Lutz", 5, 56.80], 
           ["77226", "Head First Python, Paul Barry", 3,32.95],
           ["88112", "Einführung in Python3, Bernd Klein", 	3, 24.99]]
min_order = 100

orders_total = list(map(lambda x: (x[0], x[2] * x[3]),orders))
invoice_totals = list(map(lambda x: x if x[1] > min_order else (x[0],x[1] + 10),orders_total ))
print(invoice_totals)


from functools import reduce
orders = [ [1, ("5464", 4, 9.99), ("8274",18,12.99), ("9744", 9, 44.95)], 
           [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
           [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
           [4, ("8732", 7, 11.99), ("7733",11,18.99), ("88112", 5, 39.95)] ]
min_order = 100
order_total = lambda x : list(map(lambda y: y[1] * y[2], x[1:]))
invoice_totals = list(map(lambda x : [x[0]] + order_total(x),orders))
invoice_totals = list(map(lambda x: [x[0]] + [reduce(lambda a,b: a + b,x[1:])],invoice_totals))
print(invoice_totals)