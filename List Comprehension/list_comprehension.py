Celsius = [39.2, 36.5, 37.3, 37.8]
Fahrenheit = [ ((float(9)/5)*x + 32) for x in Celsius ]
print(Fahrenheit)

"""
A Pythagorean triple consists of three positive integers a, b, and c, such that a2 + b2 = c2. 
Such a triple is commonly written (a, b, c), and the best known example is (3, 4, 5). 
The following list comprehension creates the Pythagorean triples:
"""

print(
    [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x ** 2 + y ** 2 == z ** 2]
)

colours = [ "red", "green", "yellow", "blue" ]
things = [ "house", "car", "tree" ]
coloured_things = [ (x,y) for x in colours for y in things ]
print(coloured_things)

x = ( x**2 for x in range(1,10))
print(x)
x = list(x)
print(x)

#A more Demanding Example
noprimes = [j for i in range(2,8) for j in range(i**2,100,i)]
primes = [x for x in range(2,100) if x not in noprimes]
print(primes)

from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = [j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)]
print(no_primes)

#Set Comprehension
from math import sqrt
n = 100
sqrt_n = int(sqrt(n))
no_primes = {j for i in range(2, sqrt_n+1) for j in range(i*2, n, i)}
print(type(no_primes))
primes = {i for i in range(2, n) if i not in no_primes}
print(type(primes))


#Recursive Function to Calculate the Primes

from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n + 1) if x not in no_p}
    return p
for i in range(1,50):
    print(i, primes(i))
