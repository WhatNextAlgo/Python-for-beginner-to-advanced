"""
A list can be seen as a stack. A stack in computer science is a data structure, 
which has at least two operations: one which can be used to put or push data on the stack, 
and another one to take away the most upper element of the stack.

The way of working can be imagined with a stack of plates. 
If you need a plate you will usually take the most upper one. 
The used plates will be put back on the top of the stack after cleaning. 
If a programming language supports a stack like data structure, 
it will also supply at least two operations:

•push
This method is used to put a new object on the stack. 
Depending on the point of view, we say that we "push" the object on top or attach it to the right side. 
Python doesn't offer - contrary to other programming languages - no method with the name "push", 
but the method "append" has the same functionality.

•pop
This method returns the top element of the stack. The object will be removed from the stack as well.
•peek
Some programming languages provide another method, which can be used to view what is on 
the top of the stack without removing this element. The Python list class doesn't possess such a method, 
because it is not needed. A peek can be simulated by accessing the element with the index -1:
"""

lst = ["easy", "simple", "cheap", "free"]
print(lst[-1])

lst = [3, 5, 7]
lst.append(42)
print(lst)

cities = ["Hamburg", "Linz", "Salzburg", "Vienna"]
print(cities.pop(0),cities)  

#Extend
lst = [42,98,77]
lst2 = [8,69]
lst.append(lst2)
print(lst)

lst = [42,98,77]
lst2 = [8,69]
lst.extend(lst2)
print(lst)

lst = ["a", "b", "c"]
programming_language = "Python"
lst.extend(programming_language)
print(lst)

lst = ["Java", "C", "PHP"]
t = ("C#", "Jython", "Python", "IronPython")
lst.extend(t)
print(lst)

#Extending and Appending Lists with the '+' Operator
level = ["beginner", "intermediate", "advanced"]
other_words = ["novice", "expert"]
print(level + other_words)

L = [3, 4]
L += [42]
print(L)


import time

n= 100000

start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)


start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)

start_time = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start_time)

#Removing an element with remove
colours = ["red", "green", "blue", "green", "yellow"]
colours.remove("green")
print(colours)

#Find the Position of an Element in a List
colours = ["red", "green", "blue", "green", "yellow"]
print(colours.index("green"))
print(colours.index("green", 2))
print(colours.index("yellow"))

#Insert
lst = ["German is spoken", "in Germany,", "Austria", "Switzerland"]
lst.insert(3, "and")
print(lst)

abc = ["a","b","c"]
abc.insert(len(abc),"d")
print(abc)

