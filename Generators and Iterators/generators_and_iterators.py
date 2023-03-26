"""
What is an iterator? Iterators are objects that can be iterated over like we do in a for loop. 
We can also say that an iterator is an object, which returns data, one element at a time. 
That is, they do not do any work until we explicitly ask for their next item. 
They work on a principle, which is known in computer science as lazy evaluation. 
Lazy evaluation is an evaluation strategy which delays the evaluation of an expression until 
its value is really needed. Due to the laziness of Python iterators, 
they are a great way to deal with infinity, i.e. iterables which can iterate for ever. 
You can hardly find Python programs that are not teaming with iterators.

Iterators are a fundamental concept of Python. You already learned in your first Python programs 
that you can iterate over container objects such as lists and strings. To do this, 
Python creates an iterator version of the list or string. In this case, an iterator can be seen 
as a pointer to a container, which enables us to iterate over all the elements of this container. 
An iterator is an abstraction, which enables the programmer to access all the elements of an 
iterable object (a set, a string, a list etc.) without any deeper knowledge of the 
data structure of this object.

Generators are a special kind of function, which enable us to implement or generate iterators.

Mostly, iterators are implicitly used, like in the for-loop of Python. 
We demonstrate this in the following example. We are iterating over a list, 
but you shouldn't be mistaken: A list is not an iterator, but it can be used like an iterator:
"""
cities = ["Paris", "Berlin", "Hamburg", 
          "Frankfurt", "London", "Vienna", 
          "Amsterdam", "Den Haag"]
for location in cities:
    print("location: " + location)

expertises = ["Python Beginner", 
              "Python Intermediate", 
              "Python Proficient", 
              "Python Advanced"]
expertises_iterator = iter(expertises)
print("Calling 'next' for the first time: ", next(expertises_iterator))
print("Calling 'next' for the second time: ", next(expertises_iterator))

other_cities = ["Strasbourg", "Freiburg", "Stuttgart", 
                "Vienna / Wien", "Hannover", "Berlin", 
                "Zurich"]

city_iterator = iter(other_cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city)
    except StopIteration:
        break


capitals = { 
    "France":"Paris", 
    "Netherlands":"Amsterdam", 
    "Germany":"Berlin", 
    "Switzerland":"Bern", 
    "Austria":"Vienna"}

for country in capitals:
     print("The capital city of " + country + " is " + capitals[country])


#Implementing an Iterator as a Class

"""
Implementing an Iterator as a Class
One way to create iterators in Python is defining a class which implements the 
methods __init__ and __next__. We show this by implementing a class cycle, 
which can be used to cycle over an iterable object forever. In other words, 
an instance of this class returns the element of an iterable until it is exhausted. 
Then it repeats the sequence indefinitely.
"""

class Cycle(object):
    def __init__(self,iterable):
        self.iterable = iterable
        self.iter_obj = iter(iterable)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            try:
                next_obj = next(self.iter_obj)
                return next_obj
            except StopIteration:
                self.iter_obj = iter(self.iterable)


x = Cycle("abc")
for i in range(10):
    print(next(x),end=", ")

#Generators

def city_generator():
    yield "Hamburg"
    yield "Konstanz"
    yield "Berlin"
    yield "Zurich"
    yield "Schaffhausen"
    yield "Stuttgart" 

city = city_generator()
print(next(city))
print(next(city))
print(next(city))


def count(first_value =0,step =1):
    x = first_value
    while True:
        yield x
        x += step

counter = count()
for _ in range(10):
    print(next(counter),end=", ")

start_value = 2.1
incr = 0.3
print("\nNew Counter")
counter = count(start_value,incr)
for _ in range(10):
    new_value = next(counter)
    print(f"{new_value:2.2f}",end=", ")

#Fibonacci as a Generator:

def fibonacci(n):
    a,b,counter = 0,1,0
    while True:
        if counter > n:
            return
        yield a
        a,b = b, a + b
        counter += 1

f = fibonacci(5)
for x in f:
    print(x, " ", end="") # 
print()


def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print(x, " ", end="")
    counter += 1
    if (counter > 10): 
        break 
print()


#send Method /Coroutines
"""
send Method /Coroutines
Generators can not only send objects but also receive objects. Sending a message, i.e. an object, 
into the generator can be achieved by applying the send method to the generator object. 
Be aware of the fact that send both sends a value to the generator and returns the value 
yielded by the generator. We will demonstrate this behavior in the following simple example 
of a coroutine:

"""
def simple_coroutine():
    print("coroutine has been started!")
    while True:
        x = yield 'foo'
        print("coroutine recevied: ",x)

cr = simple_coroutine()
print(next(cr))

ret_value = cr.send("Hi")
print("'send' returned: ", ret_value)

"""
We had to call next on the generator first, because the generator needed to be started. 
Using send to a generator which hasn't been started leads to an exception.

To use the send method, the generator must wait for a yield statement so that the data sent 
can be processed or assigned to the variable on the left. What we haven't said so far: 
A next call also sends and receives. It always sends a None object. 
The values sent by "next" and "send" are assigned to a variable within the generator: 
this variable is called new_counter_val in the following example.

The following example modifies the generator 'count' from the previous subchapter by adding a 
send feature.
"""

def count(first_value =0 ,step = 1):
    counter = first_value
    while True:
        new_counter_value = yield counter
        if new_counter_value is None:
            counter += step
        else:
            counter = new_counter_value

start_value = 2.1
stop_value = 0.3
counter = count(start_value, stop_value) 
for i in range(10):
    new_value = next(counter)
    print(f"{new_value:2.2f}", end=", ")
print()

print("set current count value to another value:")
counter.send(100.5)
for i in range(10):
    new_value = next(counter)
    print(f"{new_value:2.2f}", end=", ")

#Another Example for send

from random import choice

def song_generator(song_list):
    new_song = None
    while True:
        if new_song != None:
            if new_song not in song_list:
                song_list.append(new_song)
            new_song = yield new_song
        else:
            new_song = yield choice(song_list)

songs = ["Her Şeyi Yak - Sezen Aksu", 
         "Bluesette - Toots Thielemans",
         "Six Marimbas - Steve Reich",
         "Riverside - Agnes Obel",
         "Not for Radio - Nas",
         "What's going on - Taste",
         "On Stream - Nils Petter Molvær",
         "La' Inta Habibi - Fayrouz",
         "Ik Leef Niet Meer Voor Jou - Marco Borsato",
         "Δέκα λεπτά - Αθηνά Ανδρεάδη"]

radio_program = song_generator(songs)
next(radio_program)

for i in range(3):
    print(next(radio_program))

radio_program.send("Distorted Angels - Archive")
print(songs)

print("\n New Song Generator")
def song_generator_advanced(song_lists):
    new_song = None
    while True:
        if new_song != None:
            if new_song[0] == "-songlist-":
                song_lists = new_song[1]
                new_song = yield choice(song_lists)
            else:
                title, performer = new_song
                new_song = title + " - " + performer
                if new_song not in song_lists:
                    song_lists.append(new_song)
                new_song = yield choice(song_lists)
        else:
            new_song = yield choice(song_lists)

songs1 = ["Après un Rêve - Gabriel Fauré"
         "On Stream - Nils Petter Molvær",
         "Der Wanderer Michael - Michael Wollny",
         "Les barricades mystérieuses - Barbara Thompson",
         "Monday - Ludovico Einaudi"]

songs2 = ["Dünyadan Uzak - Pinhani", 
          "Again - Archive",
          "If I had a Hear - Fever Ray"
          "Every you, every me - Placebo",
          "Familiar - Angnes Obel"]
radio_prog = song_generator_advanced(songs1)
for i in range(5):
    print(next(radio_prog))

radio_prog.send(("-songlist-", songs2))

for i in range(5):
    print(next(radio_prog))

#The throw Method

print("Get the state of generator")
def count(first_value = 0,step =1):
    counter = first_value
    while True:
        try:
            new_counter_val = yield counter
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val
        except Exception:
            yield (first_value,step,counter)

c = count()
for i in range(6):
    print(next(c))
print("Let us see what the state of the iterator is:")
state_of_count = c.throw(Exception)
print(state_of_count)
print("now, we can continue:")
for i in range(3):
    print(next(c))

print("\n New StateOfGenerator class")
class StateOfGenerator(Exception):
    def __init__(self,message = None):
        self.message = message
def count(firstval=0, step=1):
    counter = firstval
    while True:
        try:
            new_counter_val = yield counter
            if new_counter_val is None:
                counter += step
            else:
                counter = new_counter_val
        except StateOfGenerator:
            yield (firstval, step, counter)

c = count()
for i in range(3):
    print(next(c))
print("Let us see what the state of the iterator is:")
i = c.throw(StateOfGenerator)
print(i)
print("now, we can continue:")
for i in range(3):
    print(next(c))

#yield from
def gen1():
    for char in "Python":
        yield char
    for i in range(5):
        yield i

def gen2():
    yield from "Python"
    yield from range(5)

g1 = gen1()
g2 = gen2()
print("g1: ", end=", ")
for x in g1:
    print(x, end=", ")
print("\ng2: ", end=", ")
for x in g2:
    print(x, end=", ")
print()

def cities():
    for city in ["Berlin", "Hamburg", "Munich", "Freiburg"]:
        yield city

def squares():
    for number in range(10):
        yield number ** 2
        
def generator_all_in_one():
    for city in cities():
        yield city
    for number in squares():
        yield number
        
def generator_splitted():
    yield from cities()
    yield from squares()
    
lst1 = [el for el in generator_all_in_one()]
lst2 = [el for el in generator_splitted()]
print(lst1 == lst2)

#recursive generator 
def permutations(items):
    n = len(items)
    if n==0: yield []
    else:
        for i in range(len(items)):
            for cc in permutations(items[:i]+items[i+1:]):
                yield [items[i]]+cc

for p in permutations(['r','e','d']): print(''.join(p))
for p in permutations(list("game")): print(''.join(p) + ", ", end="")


def k_permutations(items, n):
    if n==0: 
        yield []
    else:
        for item in items:
            for kp in k_permutations(items, n-1):
                if item not in kp:
                    yield [item] + kp
                    
for kp in k_permutations("abcd", 3):
    print(kp) 

#A Generator of Generators
def firstn(generator, n):
    g = generator()
    for i in range(n):
        yield next(g)
        
#The following script returns the first 10 elements of the Fibonacci sequence:

def fibonacci():
    """ A Fibonacci number generator """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print(list(firstn(fibonacci, 10)))  
