""" A module containing both a recursive and an iterative implementation of the Fibonacci function. 
The purpose of this module consists in showing the inefficiency of a purely recursive implementation of Fibonacci! """

def fib(n):
    """ recursive version of the Fibonacci function """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fibi(n):
    """ iterative version of the Fibonacci function """
    old, new = 0, 1
    if n == 0:
        return 0
    for i in range(n-1):
        old, new = new, old + new
    return new

"""
We can implement a "memory" for our recursive version by 
using a dictionary to save the previously calculated values. We call this version fibm:
"""
memo = {0:0, 1:1}
def fibm(n):
    if not n in memo:
        memo[n] = fibm(n-1) + fibm(n-2)
    return memo[n]