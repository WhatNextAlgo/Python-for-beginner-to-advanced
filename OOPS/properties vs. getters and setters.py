#Create a getter and setter for private attribute

class P:
    def __init__(self,x):
        self.__x = x

    def get_x(self):
        return self.__x
    
    def set_x(self,x):
        self.__x = x

p1 = P(42)
p2 = P(4711)
print(p1.get_x())
p1.set_x(47)
p1.set_x(p1.get_x()+p2.get_x())
print(p1.get_x())

"""
Let's assume we want to change the implementation like this: The attribute x can have values 
between 0 and 1000. If a value larger than 1000 is assigned, x should be set to 1000. 
Correspondingly, x should be set to 0, if the value is less than 0.
"""

class P:
    def __init__(self,x):
        self.set_x(x)

    def get_x(self):
        return self.__x
    
    def set_x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

p1 = P(1001)
print(p1.get_x())

p2 = P(15)
print(p2.get_x())

p3 = P(-1)
print(p3.get_x())

#But there is a catch: Let's assume we designed our class with the public attribute and no methods:

class P2:
    def __init__(self, x):
        self.x = x
#People have already used it a lot and they have written code like this:

p1 = P2(42)
p1.x = 1001
p1.x
"""
If we would change P2 now in the way of the class P, our new class would break the interface, 
because the attribute x will not be available anymore. That's why in Java e.g. people are recommended 
to use only private attributes with getters and setters, so that they can change the implementation 
without having to change the interface.

But Python offers a solution to this problem. The solution is called properties!

The class with a property looks like this:
"""

class P:
    def __init__(self,x):
        self.x = x

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x =x


p1 = P(1001)
print(p1.x)

"""
Alternatively, we could have used a different syntax without decorators to define the property. 
As you can see, the code is definitely 
less elegant and we have to make sure that we use the getter function in the __init__ method again:
"""

class P:
    def __init__(self,x):
        self.set_x(x)
    
    def get_x(self):
        return self.__x
    
    def set_x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(get_x,set_x)

"""
There is still another problem in the most recent version. 
We have now two ways to access or change the value of x: Either by using "p1.x = 42" or by "p1.set_x(42)".
 This way we are violating one of the fundamentals of Python: "There should be one-- and preferably 
 only one --obvious way to do it." (see Zen of Python)

We can easily fix this problem by turning the getter and the setter methods into private methods, 
which can't be accessed anymore by the users of our class P:
"""

class P:
    def __init__(self,x):
        self.__set_x(x)
    
    def __get_x(self):
        return self.__x
    
    def __set_x(self,x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    x = property(__get_x,__set_x)

"""
Even though we fixed this problem by using a private getter and setter, the version with 
the decorator "@property" is the Pythonic way to do it!

From what we have written so far, and what can be seen in other books and tutorials as well, 
we could easily get the impression that there is a one-to-one connection between properties 
(or mutator methods) and the attributes, i.e. that each attribute has or should have its own 
property (or getter-setter-pair) and the other way around. Even in other object oriented languages 
than Python, it's usually not a good idea to implement a class like that. 
The main reason is that many attributes are only internally needed and creating interfaces for the 
user of the class increases unnecessarily the usability of the class. The possible user of a class 
shouldn't be "drowned" with umpteen - of mainly unnecessary - methods or properties!

The following example shows a class, which has internal attributes, which can't be accessed from outside.
 These are the private attributes self.__potential _physical and self.__potential_psychic. 
 Furthermore we show that a property can be deduced from the values of more than one attribute. 
 The property "condition" of our example returns the condition of the robot in a descriptive string. 
 The condition depends on the sum of the values of the psychic and the physical conditions of the robot.
"""

class Robot:
    def __init__(self, name, build_year, lk = 0.5, lp = 0.5 ):
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp
    @property
    def condition(self):
        s = self.__potential_physical + self.__potential_psychic
        if s <= -1:
           return "I feel miserable!"
        elif s <= 0:
           return "I feel bad!"
        elif s <= 0.5:
           return "Could be worse!"
        elif s <= 1:
           return "Seems to be okay!"
        else:
           return "Great!" 

x = Robot("Marvin", 1979, 0.2, 0.4 )
y = Robot("Caliban", 1993, -0.4, 0.3)
print(x.condition)
print(y.condition)

#Public instead of Private Attributes
"""
Let's summarize the usage of private and public attributes, getters and setters, and properties: 
Let's assume that we are designing a new class and we pondering about an instance or class attribute
 "OurAtt", which we need for the design of our class. We have to observe the following issues:

Will the value of "OurAtt" be needed by the possible users of our class?
If not, we can or should make it a private attribute.
If it has to be accessed, we make it accessible as a public attribute
We will define it as a private attribute with the corresponding property, if and only 
if we have to do some checks or transformation of the data. (As an example, you can have a look 
again at our class P, where the attribute has to be in the interval between 0 and 1000, 
which is ensured by the property "x")
Alternatively, you could use a getter and a setter, but using a property is the Pythonic way
 to deal with it!
Let's assume we defined "OurAtt" as a public attribute. Our class has been successfully used
 by other users for quite a while.
"""

class OurClass:
    def __init__(self, a):
        self.OurAtt = a
x = OurClass(10)
print(x.OurAtt)
"""
Now comes the point which frightens some traditional OOPistas out of their wits: Imagine "OurAtt" has 
been used as an integer. Now, our class has to ensure that "OurAtt" has to be a value between 0 and 1000? Without property, this is 
really a horrible scenario! Due to properties it's easy: We create a property version of "OurAtt".
"""
class OurClass:
    def __init__(self, a):
        self.OurAtt = a
    @property
    def OurAtt(self):
        return self.__OurAtt
    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val
x = OurClass(10)
print(x.OurAtt)

"""
This is great, isn't it? You can start with the simplest implementation imaginable, 
and you are free to later migrate to a property version without having to change the 
interface! So properties are not just a replacement for getters and setters!

Something else you might have already noticed: For the users of a class, 
properties are syntactically identical to ordinary attributes.
"""