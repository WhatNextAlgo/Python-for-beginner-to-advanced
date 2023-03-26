"""
Recursion is a method of programming or coding a problem, 
in which a function calls itself one or more times in its body. 
Usually, it is returning the return value of this function call. 
If a function definition satisfies the condition of recursion, 
we call this function a recursive function.
Termination condition: A recursive function has to fulfil an important condition to be used in a program:
it has to terminate. A recursive function terminates, if with every recursive call the solution of 
the problem is downsized and moves towards a base case. A base case is a case, 
where the problem can be solved without further recursion. A recursion can end up in an infinite loop, 
if the base case is not met in the calls.
"""

#Recursive Functions in Python

#Now we come to implement the factorial in Python. 
# It's as easy and elegant as the mathematical definition.

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 0:return 1
    res = n * factorial(n - 1)
    print("intermediate result for ",n," * factorial(",n-1,"): ",res)
    return res

print(factorial(5))

#Let's have a look at an iterative version of the factorial function.
def iterative_factorial(n):
    result = 1
    for i in range(2,n + 1):
        result *= i
    return result

for i in range(5):
    print(i, iterative_factorial(i))



from timeit import Timer

t1 = Timer("fib(10)","from fibonacci import fib")

for i in range(1, 20):
    cmd = "fibm(" + str(i) + ")"
    t1 = Timer(cmd, "from fibonacci import fibm")
    time1 = t1.timeit(3)
    cmd = "fibi(" + str(i) + ")"
    t2 = Timer(cmd, "from fibonacci import fibi")
    time2 = t2.timeit(3)
    print(f"n={i:2d}, fibm: {time1:8.6f}, fibi:  {time2:7.6f}, time1/time2: {time1/time2:10.2f}")
    

"""
We can also define a recursive algorithm for our Fibonacci function by 
using a class with callabe instances, i.e. by using the special method call. 
This way, we will be able to hide the dictionary in an elegant way. 
We used a general approach which allows as to define also functions similar to Fibonacci, 
like the Lucas function. This means that we can create Fibonacci-like 
number sequences by instantiating instances of this class. Basically, 
the building principle, i.e. the sum of the previous two numbers, will be the same. 
They will differ by the two initial values:
"""

class FibonacciLike:
    def __init__(self,i1=0,i2=1):
        self.memo ={0:i1,1:i2}

    def __call__(self,n):
        if n not in self.memo:
            self.memo[n] = self.__call__(n-1) + self.__call__(n - 2)
        return self.memo[n]
    
# We create a callable to create the Fibonacci numbers:
fib = FibonacciLike()

# This will create a callable to create the Lucas number series:
lucas = FibonacciLike(2, 1)

for i in range(1, 16):
    print(i, fib(i), lucas(i))


class kFibonacci:

    def __init__(self, k, initials, coefficients):
        self.memo = dict(zip(range(k), initials))
        self.coeffs = coefficients
        self.k = k

    def __call__(self, n):
        k = self.k
        if n not in self.memo: 
            result = 0
            for coeff, i in zip(self.coeffs, range(1, k+1)):
                result += coeff * self.__call__(n-i)
            self.memo[n] = result  
        return self.memo[n]
    
fib = kFibonacci(2, (0, 1), (1, 1))
lucas = kFibonacci(2, (2, 1), (1, 1))

for i in range(1, 16):
    print(i, fib(i), lucas(i))

P = kFibonacci(2, (1, 2), (2, 1))
for i in range(10):
    print(i, P(i))

def nP(n):
    if n < 2:
        return P(n)
    else:
        i = n // 2 + 1
        if n % 2:  # n is odd
            return P(i)
        else:
            return P(i-1) + P(i-2)
            
for i in range(20):
    print(nP(i), end=", ")

nP = kFibonacci(4, (1, 2, 3, 5), (0, 2, 0, 1))
for i in range(20):
    print(nP(i), end=", ")

sqrt2 = 2 ** 0.5
print("Square root of 2: ", sqrt2)
print("Square root of 3: ", 1 + 1 / sqrt2)
for i in range(1, 20):
    print(nP(i) / nP(i-1), end=", ")
        