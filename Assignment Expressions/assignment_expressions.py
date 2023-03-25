"""
We will introduce this way of assignment in this part of our Python tutorial.
A simple assignment can also be replaced by an assignment expression, 
even though it looks clumsy and is definitely not the intended use case of it:

"""
x = 5 
# can be wriiten as:
(x := 5) # valid, but not recommeded!
# the bracket are crucial

#Let's look at a little Code example which only uses traditional assignments:
txt = 'Python needs training!'
ideal_length = 22
n = len(txt)
if (n == ideal_length):
    print(f"The length {n} is ideal!")
else:
    print(f"{n} is not ideal!")

#We will use the new walrus operator in the following Python code snippet:
txt = 'Python needs training!'
ideal_length = 22
if (n := len(txt)) == ideal_length:
    print(f"The length {n} is ideal!")
else:
    print(f"{n} is not ideal!")

#Beneficial applications of the Assignment Expressions
#List Comprehension

#In the following you will see a list comprehension with a walrus operator:

def f(x):return x + 4

numbers = [3,7,2,9,12]
odd_numbers = [result for x in numbers if (result := f(x)) % 2 != 0 ]
print(odd_numbers)

#The above implementation is more efficient than a list comprehension without the assignment expression, 
# because we will have to call the function twice:

odd_numbers = [f(x) for x in numbers if  f(x) % 2]
print(odd_numbers)


"""
Regular Expressions
There is also a big advantage when we use regular expressions:
"""

import re

txt = """The Python training course started at 2022-02-4 
the other one at 2022-01-24
only one date per line, if at all
the dates may also be in this format 2020/10/15
or 20-10-04"""

for line in txt.split("\n"):
    if (date := re.search(r'(\d{2,4})[-/](\d{2})[-/](\d{2})',line)):
        year, month, day = date.groups()
        print(year, month, day)


#Usage in while Loops
import random
lower_bound, upper_bound = 1,20
to_be_guessed = random.randint(lower_bound,upper_bound)
guess = 0
while guess != to_be_guessed:
    guess = int(input("New Number: "))
    if guess > to_be_guessed:
        print("Number too large")
    elif guess < to_be_guessed:
        print("Number too small")
else:
    print("Congratulations, You made it!")

"""
As you can see, we had to initialize guess to zero to be able to enter the loop. 
We can do the initialization directly in the loop condition 
with an assignment expression and simplify the whole code by this:
"""
import random
lower_bound, upper_bound = 1,20
to_be_guessed = random.randint(lower_bound,upper_bound)
while (guess := int(input("New Number: "))) != to_be_guessed:
    if guess > to_be_guessed:
        print("Number too large")
    elif guess < to_be_guessed:
        print("Number too small")
else:
    print("Congratulations, You made it!")


#Taken to the extreme:

"""
Taken to the extreme:
We said in the beginning of this page that some Python programmers longed for this consstruct for 
quite a while. One reason why it was not introduced earlier was the fact that it can also be used 
to write code which is less readable if used to extensivel. 
The following code snippet is showing such an extreme example which is not recommended to use:
"""

a,b,c = 1,2,3
x = 4
y = (c := (a := x*2.3) + (b := x*4.5 -3))
print(y)
