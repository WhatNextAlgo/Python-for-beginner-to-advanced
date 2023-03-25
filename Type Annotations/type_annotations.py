"""
In this example you see the ord()function, 
which takes a string as input and converts it into an integer by 
using the ASCII values of the letters it contains.
"""

def my_functions(a:int,b:str)->int:
    return a + ord(b)

print(my_functions(3,'a'))

"""
Interestingly our function runs now, 
yet our argument a is of type float and not integer as we declared at the very beginning.
"""
print(my_functions(4.2,'a'))

"""
In this example, we are going to see how the functions 
can be given variables that can work without raising any errors. 
However, that can be still be very problematic.
"""

def add_together(a:int,b:int)->int:
    return a + b 
def return_the_last_digit(a:int)->int:
    return a % 10
our_sum = add_together(38,57)
print(return_the_last_digit(our_sum))