"""
Introduction:

Sequences are one of the principal built-in data types besides 
numerics, mappings, files, instances and exceptions. 
Python provides for six sequence (or sequential) data types:

strings
byte sequences
byte arrays
lists
tuples
range objects
Strings, lists, tuples, bytes and range objects may look like utterly different things, 
but they still have some underlying concepts in common:

The items or elements of strings, lists and tuples are ordered in a defined sequence
The elements can be accessed via indices
"""

text = "Lists and Strings can be accessed via indices!"
print(text[0],text[10],text[-1])

#Accessing lists:

cities = ["Vienna", "London", "Paris", 
          "Berlin", "Zurich", "Hamburg"]
print(cities[0])
print(cities[2])
print(cities[-1]) 

"""
Unlike other programming languages Python uses the same syntax and 
function names to work on sequential data types. For example, 
the length of a string, a list, and a tuple can be determined with a function called len():
"""
countries = ["Germany", "Switzerland", "Austria", 
             "France", "Belgium", "Netherlands", 
             "England"]
len(countries)  # the length of the list, i.e. the number of objects

fib = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
len(fib)

#Accessing List elements

languages = ["Python", "C", "C++", "Java", "Perl"]
languages = ["Python", "C", "C++", "Java", "Perl"]
print(languages[0] + " and " + languages[1] + " are quite different!") 
print("Accessing the last element of the list: " + languages[-1]) 

person = [["Marc", "Mayer"], 
          ["17, Oxford Str", "12345", "London"], 
          "07876-7876"]
name = person[0]
print(name)

first_name = person[0][0]
print(first_name)

last_name = person[0][1]
print(last_name)

address = person[1]
print(address)

street = person[1][0]
print(street)

complex_list = [["a", ["b", ["c", "x"]]]]
complex_list = [["a", ["b", ["c", "x"]]], 42]
print(complex_list[0][1])

print(complex_list[0][1][1][0])

#Changing list

languages = ["Python", "C", "C++", "Java", "Perl"]
languages[4] = "Lisp"
print(languages)

languages.append("Haskell")
print(languages)

languages.insert(1, "Perl")
print(languages)

shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']
cart = []
#  "pop()"" removes the last element of the list and returns it
article = shopping_list.pop()  
print(article, shopping_list)
cart.append(article)
print(cart)

# we go on like this:
article = shopping_list.pop()  
print("shopping_list:", shopping_list)
cart.append(article)
print("cart: ", cart)

#With a while loop:
shopping_list = ['milk', 'yoghurt', 'egg', 'butter', 'bread', 'bananas']
cart = []

while shopping_list != []:
    article = shopping_list.pop()
    cart.append(article)
    print(article,shopping_list)

print("shopping_list: ", shopping_list)
print("cart: ", cart)

#Tuples
"""
A tuple is an immutable list, i.e. a tuple cannot be changed in any way, once it has been created. 
A tuple is defined analogously to lists, except the set of elements is enclosed in parentheses 
instead of square brackets. The rules for indices are the same as for lists. 
Once a tuple has been created, you can't add elements to a tuple or remove elements from a tuple.
"""
t = ("tuples", "are", "immutable")
print(t[0])

#Slicing
slogan = "Python is great"
first_six = slogan[0:6]
print(first_six)

starting_at_five = slogan[5:]
print(starting_at_five)

a_copy = slogan[:]
without_last_five = slogan[0:-5]
print(without_last_five)

cities = ["Vienna", "London", "Paris", "Berlin", "Zurich", "Hamburg"]
first_three = cities[0:3]
print(first_three)

all_but_last_two = cities[:-2]
print(all_but_last_two)

slogan = "Python under Linux is great"
print(slogan[::3])

s = "TPoyrtohnotno  ciosu rtshees  lianr gTeosrto nCtiot yb yi nB oCdaennasdeao"
print(s)
print(s[::2])
print(s[1::2])

s = "Toronto is the largest City in Canada"
t = "Python courses in Toronto by Bodenseo"
s = "".join(["".join(x) for x in zip(s,t)])
print(s)

#Concatenation of Sequences
firstname = "Homer"
surname = "Simpson"
name = firstname + " " + surname
print(name) 

colours1 = ["red", "green","blue"]
colours2 = ["black", "white"]
colours = colours1 + colours2
print(colours)

#Checking if an Element is Contained in List
abc = ["a","b","c","d","e"]
print("a" in abc)
print("a" not in abc)
print("e" not in abc)

#Repetitions
print(3 * "xyz-")
print(3  * ["a","b","c"])

#The Pitfalls of Repetitions
x = ["a","b","c"]
y = [x] * 4
print(y)

y[0][0] = "p"
print(y)