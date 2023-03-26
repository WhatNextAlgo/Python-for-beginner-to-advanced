"""
So what is the difference between an iterable and an iterator?
On one hand, they are the same: You can iterate with a for loop over iterators and iterables. 
Every iterator is also an iterable, but not every iterable is an iterator. 
E.g. a list is iterable but a list is not an iterator! An iterator can be created from an 
iterable by using the function 'iter'. To make this possible the class of an object needs 
either a method '__iter__', which returns an iterator, or a '__getitem__' method with sequential 
indexes starting with 0.

Iterators are objects with a '__next__' method, which will be used when the function 'next()' 
is called.So what is going on behind the scenes, when a for loop is executed? 
The for statement calls iter() on the object ( which should be a so-called container object), 
over which it is supposed to loop . If this call is successful, 
the iter call will return an iterator object that defines the method __next__() 
which accesses elements of the object one at a time. The __next__() method will 
raise a StopIteration exception, if there are no further elements available. 
The for loop will terminate as soon as it catches a StopIteration exception. 
You can call the __next__() method using the next() built-in function. This is how it works:
"""

cities = ["Berlin", "Vienna", "Zurich"]
iterator_obj = iter(cities)
print(iterator_obj)
print(next(iterator_obj))
print(next(iterator_obj))
print(next(iterator_obj))

def iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

for element in [34,[4,5],(4,5),{"a":4},"adfgr",4.5]:
    print(element,iterable(element))

class Reverse:
    """
    Creates Iterators for looping over a sequence backwards.
    """
    def __init__(self,data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
    
lst = [34, 978, 42]
lst_backwards = Reverse(lst)
for el in lst_backwards:
    print(el)