#OOP in Python
"""
Even though we haven't talked about classes and object orientation in previous chapters, 
we have worked with classes all the time. In fact, everything is a class in Python. 
Guido van Rossum has designed the language according to the principle "first-class everything". 
He wrote: "One of my goals for Python was to make it so that all objects were "first class." 
By this, I meant that I wanted all objects that could be named in the language 
(e.g., integers, strings, functions, classes, modules, methods, and so on) to have equal status. 
That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as 
arguments, and so forth." (Blog, The History of Python, February 27, 2009) In other words, 
"everything" is treated the same way, everything is a class: functions and methods are values 
just like lists, integers or floats. Each of these are instances of their corresponding classes.
"""
x = 42
print(type(x))
y = 4.34
print(type(y))

def f(x):
    return x + 1

print(type(f))

class Robert:
    pass

x = Robert()
y = Robert()
y1 = y
print(x == y)
print(y == y1)

"""
Attribute:
Let's get back to Python: We will learn later that properties and attributes are essentially 
different things in Python. This subsection of our tutorial is about attributes in Python. 
So far our robots have no attributes. Not even a name, like it is customary for ordinary robots, 
isn't it? So, let's implement a name attribute. 
"type designation", "build year" etc. are easily conceivable as further attributes as well***.

Attributes are created inside a class definition, as we will soon learn. We can dynamically
 create arbitrary new attributes for existing instances of a class. We do this by joining an 
 arbitrary name to the instance name, separated by a dot ".". In the following example, 
 we demonstrate this by creating an attribute for the name and the year built:
"""

class Robert:
    pass
x = Robert()
y = Robert()
x.name = "Marvin"
x.build_year = "1979"
y.name = "Caliban"
y.build_year = "1993"

print(x.name)
print(x.__dict__)
print(y.__dict__)
#Attributes can be bound to class names as well. In this case, 
# each instance will possess this name as well. Watch out, 
# what happens, if you assign the same name to an instance:

Robert.brand = "Kuku"
print(x.brand)
x.brand = "Thales"
print(Robert.brand)
print(Robert.__dict__)
print(x.__dict__)

"""
If you try to access y.brand, Python checks first, if "brand" is a key of the y. __dict__ dictionary. 
If it is not, Python checks,if "brand" is a key of the Robot. __dict__. If so, the value can be retrieved.

If an attribute name is not in included in either of the dictionary, the attribute name is not defined. 
If you try to access a non-existing attribute, you will raise an AttributeError:
"""

# x.energy # AttributeError: 'Robot' object has no attribute 'energy'

#By using the function getattr, you can prevent this exception, if you provide a default value as
#  the third argument:

print(getattr(x,'energy',100))
print(x.__dict__,"\n",Robert.__dict__)

"""
Binding attributes to objects is a general concept in Python. 
Even function names can be attributed. You can bind 
an attribute to a function name in the same way, we have done so far to other instances of classes:
"""

def f(x):
    return 42
f.x = 45
print(f.x)
"""
This can be used as a replacement for the static function variables of C and C++, 
which are not possible in Python. We use a counter attribute in the following example:
"""

def f(x):
    f.counter = getattr(f,'counter',0) + 1
    return "Monty Python"
for i in range(10):
    f(i)
print(f.__dict__,f.counter)

#Methods

"""
Methods in Python are essentially functions in accordance with Guido's saying "first-class everything".

Let's define a function "hi", which takes an object "obj" as an argument and assumes that 
this object has an attribute "name". We will also define our basic Robot class again:
"""

def hi(obj):
    print("Hi, I am " + obj.name + "!" + " and my class name: " + str(obj.__class__))

class Robert:
    say_hi = hi # avoid doing this
x = Robert()
x.name = "Marvin"
hi(x)
Robert.say_hi(x)
x.say_hi()

#The __init__ Method

class A:
    def __init__(self,name = None):
        print("__init__ has been executed")
        self.name = name

    #class method
    def say_hi(self):
        if self.name:
            print("Hi, I am "+ self.name)
        else:
            print("Hi, I am a robert without a name")
x = A()
x.say_hi()
y = A("Marvin")
y.say_hi()

#Data Abstraction, Data Encapsulation, and Information Hiding

"""
Data Abstraction, Data Encapsulation and Information Hiding are often synonymously used in books and tutorials on OOP. However, 
there is a difference. Encapsulation is seen as the bundling of data with the methods that operate 
on that data. Information hiding on the other hand is the principle that some internal information 
or data is "hidden", so that it can't be accidentally changed. Data encapsulation 
via methods doesn't necessarily mean that the data is hidden. You might be capable 
of accessing and seeing the data anyway, but using the methods is recommended. 
Finally, data abstraction is present, if both data hiding and data encapsulation is used. 
In other words, data abstraction is the broader term:

Data Abstraction = Data Encapsulation + Data Hiding

Encapsulation is often accomplished by providing two kinds of methods for attributes: 
The methods for retrieving or accessing the values of attributes are called getter methods. 
Getter methods do not change the values of attributes, they just return the values. 
The methods used for changing the values of attributes are called setter methods.

We will define now a Robot class with a Getter and a Setter for the name attribute. 
We will call them get_name and set_name accordingly.
"""

class Robot:
    def __init__(self,name = None,build_year=None):
        self.name = name
        self.build_year = build_year
    
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created!")

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name

    def get_build_year(self):
        return self.build_year
    
    def set_build_year(self,build_year):
        self.build_year = build_year

x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())

x = Robot("Henry", 2008)
y = Robot()
y.set_name("Marvin")
x.say_hi()
y.say_hi()


#__str__- and __repr__-Methods
"""
We will have a short break in our treatise on data abstraction for a quick side-trip. 
We want to introduce two important magic methods "__str__" and "__repr__", 
which we will need in future examples. In the course of this tutorial, 
we have already encountered the __str__ method. We had seen that we can depict various data as string 
by using the str function, which uses "magically" the internal __str__ method of the corresponding 
data type.
 __repr__ is similar. It also produces a string representation
"""
l = ["Python", "Java", "C++", "Perl"]
print(l)
print(str(l))
print(repr(l))

"""
If you apply str or repr to an object, Python is looking for a corresponding 
method __str__ or __repr__ in the class definition of the object. If the method does exist, 
it will be called. In the following example, we define a class A, having neither 
a __str__ nor a __repr__ method. We want to see, what happens, 
if we use print directly on an instance of this class, or if we apply str or repr to this instance:
"""
class A:
    pass
a = A()
print(a)

print(str(a))
print(repr(a))

"""
As both methods are not available, Python uses the default output for our object "a".

If a class has a __str__ method, the method will be used for an instance x of that class, 
if either the function str is applied to it or if it is used in a print function. 
__str__ will not be used, 
if repr is called, or if we try to output the value directly in an interactive Python shell:
"""
class A:
    def __str__(self):
        return "42"
    
a = A()
print(repr(a))
print(str(a))

"""
Otherwise, if a class has only the __repr__ method and no __str__ method,
__repr__ will be applied in the situations, where __str__ would be applied, if it were available:
"""
class A:
    def __repr__(self):
        return "42"
a = A()
print(repr(a))
print(str(a))
print(a)

"""
A frequently asked question is when to use __repr__ and when __str__. __str__ is always the right choice,
if the output should be for the end user or in other words, if it should be nicely printed.
__repr__ on the other hand is used for the internal representation of an object. 
The output of __repr__ should be - if feasible - a string which can be parsed by the python interpreter.
The result of this parsing is in an equal object. That is, the following should be true for an object "o":

 o == eval(repr(o)) 
"""

l = [3,8,9]
s = repr(l)
print(s)

print(l == eval(s))
print(l == eval(str(l)))
"""
We show in the following example with the datetime module that eval can only be applied on the 
strings created by repr:
"""
import datetime
today = datetime.datetime.now()
str_s = str(today)
# eval(str_s) # raise SyntaxError: invalid token
repr_s = repr(today)
print(repr_s)
t = eval(repr_s)
print(type(t))


class Robot:
    def __init__(self,name,build_year):
        self.name = name
        self.build_year = build_year
    
    def __repr__(self) -> str:
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"
    
x = Robot("Sumit","1993")
x_str = str(x)
print(x_str)
print("Type of x_str: ",type(x_str))
new = eval(x_str)
print(new)
print("Type of new:", type(new))

#Public, - Protected-, and Private Attributes

class A():
    def __init__(self):
        self.__priv = "I am private"
        self._prot = "I am protected"
        self.pub = "I am public"

x = A()
x.pub = x.pub + " and my value can be changed"
print(x.pub)
print(x._prot)

# print(x.__priv) # AttributeError: 'A' object has no attribute '__priv'


class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name    
    def set_build_year(self, by):
        self.__build_year = by
    def get_build_year(self):
        return self.__build_year    
    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"
    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)
if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")


"""
Destructor
What we said about constructors holds true for destructors as well. There is no "real" destructor, 
but something similar, i.e. the method __del__. It is called when the instance is about to be destroyed 
and if there is no other reference to this instance. If a base class has a __del__() method, 
the derived class's __del__() method, if any, must explicitly call it to ensure proper deletion 
of the base class part of the instance.

The following script is an example with __init__ and __del__:

"""
class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print ("Robot has been destroyed")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y
"""
The usage of the __del__ method is very problematic. 
If we change the previous code to personalize the deletion of a robot, we create an error:
"""

class Robot():
    def __init__(self, name):
        print(name + " has been created!")
    def __del__(self):
        print (self.name + " says bye-bye!")
if __name__ == "__main__":
    x = Robot("Tik-Tok")
    y = Robot("Jenkins")
    z = x
    print("Deleting x")
    del x
    print("Deleting z")
    del z
    del y