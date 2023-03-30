"""
Definition of Memoization
The term "memoization" was introduced by Donald Michie in the year 1968. 
It's based on the Latin word memorandum, meaning "to be remembered". 
It's not a misspelling of the word memorization, though in a way it has something in common. 
Memoisation is a technique used in computing to speed up programs. 
This is accomplished by memorizing the calculation results of processed input 
such as the results of function calls. If the same input or a function call with the 
same parameters is used, the previously stored results can be used again and unnecessary 
calculation are avoided. In many cases a simple array is used for storing the results, 
but lots of other structures can be used as well, such as associative arrays, 
called hashes in Perl or dictionaries in Python.

Memoization can be explicitly programmed by the programmer, but some programming languages 
like Python provide mechanisms to automatically memoize functions.
"""

"""
Memoization with Function Decorators
You may consult our chapter on decorators as well. Especially, 
if you may have problems in understanding our reasoning.

In our previous chapter about recursive functions, we worked out an iterative and a recursive version 
to calculate the Fibonacci numbers. We have shown that a direct implementation of the mathematical 
definition into a recursive function like the following has an exponential runtime behaviour:
"""

def fib(n):
    if n == 0:return 0
    elif n == 1:return 1
    else: return fib(n - 1) + fib(n -2)


"""
We also presented a way to improve the runtime behaviour of the recursive version by adding a 
dictionary to memorize previously calculated values of the function. 
This is an example of explicitly using the technique of memoization, but we didn't call it like this. 
The disadvantage of this method is that the clarity and the beauty of the original 
recursive implementation is lost.

The "problem" is that we changed the code of the recursive fib function. 
The following code doesn't change our fib function, so that its clarity and legibility isn't touched. 
To this purpose, we define and use a function which we call memoize. memoize() takes a function as 
an argument. The function memoize uses a dictionary "memo" to store the function results. 
Though the variable "memo" as well as the function "f" are local to memoize, 
they are captured by a closure through the helper function which is returned as a reference by memoize(). 
So, the call memoize(fib) returns a reference to the helper() which is doing what fib() 
would do on its own plus a wrapper which saves the calculated results. 
For an integer 'n' fib(n) will only be called, if n is not in the memo dictionary. 
If it is in it, we can output memo[n] as the result of fib(n).
"""

def memoize(func):
    memo ={}
    def helper(x):
        if x not in memo:
            memo[x] = func(x)
            return memo[x]
        return memo[x]
    
    return helper

@memoize
def fib(n):
    if n == 0:return 0
    elif n == 1:return 1
    else: return fib(n - 1) + fib(n -2)


# fib = memoize(fib) # with out decorator
print(fib(40)) # with decorator

#Using a Callable Class for Memoization

class Memoize:
    def __init__(self,fn):
        self.fn = fn
        self.memo = {}
    
    def __call__(self,*args):
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]
    
@Memoize
def fib2(n):
    if n == 0:return 0
    elif n == 1:return 1
    else: return fib2(n - 1) + fib2(n -2)  
print(fib2(40))  



def factors_set():
        for i in [-1, 0, 1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    for l in [-1,0,1]:
                        yield (i, j, k, l)  
def memoize(f):
    results = {}
    def helper(n):
        if n not in results:
            results[n] = f(n)
        return results[n]
    return helper
@memoize
def linear_combination(n):
    """ returns the tuple (i,j,k,l) satisfying
        n = i*1 + j*3 + k*9 + l*27      """
    weighs = (1,3,9,27)
    for factors in factors_set():
       sum = 0
       for i in range(len(factors)):
          sum += factors[i] * weighs[i]
       if sum == n:
          return factors 
#With this, it is easy to write our function weigh().

def weigh(pounds):
        weights = (1, 3, 9, 27)
        scalars = linear_combination(pounds)
        left = ""
        right = ""
        for i in range(len(scalars)):
            if scalars[i] == -1:
                left += str(weights[i]) + " "
            elif scalars[i] == 1:
                right += str(weights[i]) + " "
        return (left,right)
for i in [2, 3, 4, 7, 8, 9, 20, 40]:
            pans = weigh(i)
            print("Left  pan: " + str(i) + " plus " + pans[0])
            print("Right pan: " + pans[1] + "\n")    


        
