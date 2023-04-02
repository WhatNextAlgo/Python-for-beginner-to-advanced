"""
Class Attributes
Instance attributes are owned by the specific instances of a class. That is, for two different instances,
 the instance attributes are usually different. You should by now be familiar with this concept which 
 we introduced in our previous chapter.

We can also define attributes at the class level. Class attributes are attributes which are 
owned by the class itself. They will be shared by all the instances of the class. 
Therefore they have the same value for every instance. We define class attributes 
outside all the methods, usually they are placed at the top, right below the class header.

"""

class A:
    a = "I am a class attribute!"

x = A()
y = A()
print(x.a,y.a)

"""
But be careful, if you want to change a class attribute, 
you have to do it with the notation ClassName.AttributeName. 
Otherwise, you will create a new instance variable. We demonstrate this in the following example:
"""

x.a = "This will create a new instance attribute for x!"
print(y.a,"\n",A.a,A.__dict__,"\n",x.a,x.__dict__)

#Example with Class Attributes

class Robot:
    Three_Laws = (
    """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
    """A robot must obey the orders given to it by human beings, except where such orders would conflict
    with First Law.,""",
    """A robot must protect its own existence as long as such projection does not comflict with the First
    and Second Law."""
    )

    def __init__(self,name,build_year):
        self.name = name
        self.build_year = build_year

for number, text in enumerate(Robot.Three_Laws):
    print(str(number+1) + ":\n" + text) 


"""
In the following example, we demonstrate, how you can count instance with class attributes. 
All we have to do is

to create a class attribute, which we call "counter" in our example
to increment this attribute by 1 every time a new instance is created
to decrement the attribute by 1 every time an instance is destroyed
"""

class C:
    counter = 0
    def __init__(self):
        type(self).counter += 1
    def __del__(self):
        type(self).counter -= 1

x = C()
print("Number of instances: : " + str(C.counter),"class counter: " + str(C.counter))
y = C()
print("Number of instances: : " + str(C.counter),"class counter: "+ str(C.counter))
del x
print("Number of instances: : " + str(C.counter),"class counter: "+ str(C.counter))
del y
print("Number of instances: : " + str(C.counter),"class counter: "+ str(C.counter))

"""
Principially, we could have written C.counter instead of type(self).counter, 
because type(self) will be evaluated to "C" anyway. 
However we will understand later, that type(self) makes sense, if we use such a class as a superclass.
"""

#Static Methods
"""
We used class attributes as public attributes in the previous section. 
Of course, we can make public attributes private as well. We can do this by adding 
the double underscore again. If we do so, we need a possibility 
to access and change these private class attributes. We could use instance methods for this purpose:
"""
class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances(self):
        return Robot.__counter
if __name__ == "__main__":
    x = Robot()
    print(x.RobotInstances())
    y = Robot()
    print(x.RobotInstances())

"""
This is not a good idea for two reasons: First of all, because the number of robots 
has nothing to do with a single robot instance and secondly because we can't inquire 
the number of robots before we create an instance. If we try to invoke the method with the 
class name Robot.RobotInstances(), we get an error message, because it needs an instance as an argument:
"""

#Robot.RobotInstances() #TypeError: RobotInstances() missing 1 required positional argument: 'self'
#The next idea, which still doesn't solve our problem, is omitting the parameter "self":

class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter += 1
    def RobotInstances():
        return Robot.__counter
#Now it's possible to access the method via the class name, but we can't call it via an instance:


print(Robot.RobotInstances())
x = Robot()
#x.RobotInstances() # RobotInstances() takes 0 positional arguments but 1 was given
"""
The call "x.RobotInstances()" is treated as an instance method call and an instance method needs 
a reference to the instance as the first parameter.

So, what do we want? We want a method, which we can call via the class name or 
via the instance name without the necessity of passing a reference to an instance to it.

The solution lies in static methods, which don't need a reference to an instance. 
It's easy to turn a method into a static method. All we have to do is to add a line with 
"@staticmethod" directly in front of the method header. It's the decorator syntax.

You can see in the following example that we can now use our method RobotInstances the way we want:
"""

class Robot:
    __counter = 0 # private attribute
    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return Robot.__counter 
print("\nstatic method:\n",Robot.RobotInstances())
x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
print(Robot.RobotInstances())

#Class Methods
"""
Static methods shouldn't be confused with class methods. Like static methods class methods are not 
bound to instances, but unlike static methods class methods are bound to a class. 
The first parameter of a class method is a reference to a class, i.e. a class object. 
They can be called via an instance or the class name.
"""

class Robot:
    __counter = 0
    def __init__(self):
        type(self).__counter +=1
    
    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter
    
print(Robot.RobotInstances())
x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
print(Robot.RobotInstances())

"""
The use cases of class methods:

They are used in the definition of the so-called factory methods, which we will not cover here.
They are often used, where we have static methods, which have to call other static methods. To do this, 
we would have to hard code the class name, if we had to use static methods. This is a problem, 
if we are in a use case, where we have inherited classes.
The following program contains a fraction class, which is still not complete. 
If you work with fractions, you need to be capable of reducing fractions, 
e.g. the fraction 8/24 can be reduced to 1/3. We can reduce a fraction to lowest terms 
by dividing both the numerator and denominator by the Greatest Common Divisor (GCD).

We have defined a static gcd function to calculate the greatest common divisor of two numbers. 
the greatest common divisor (gcd) of two or more integers (at least one of which is not zero), 
is the largest positive integer that divides the numbers without a remainder. 
For example, the 'GCD of 8 and 24 is 8. The static method "gcd" is called by our 
class method "reduce" with "cls.gcd(n1, n2)". "CLS" is a reference to "fraction".
"""

class Fraction:
    def __init__(self,n,d):
        self.nummerator,self.denominator = Fraction.reduce(n,d)
    
    @staticmethod
    def gcd(a,b):
        while b != 0:
            a,b = b, a%b
        return a
    
    @classmethod
    def reduce(cls,n1,d1):
        g = cls.gcd(n1,d1)
        return (n1//g,d1//g)
    
    def __str__(self):
        return str(self.nummerator) +"/"+ str(self.denominator)
    

x = Fraction(8,24)
print(x)

"""
Class Methods vs. Static Methods and Instance Methods
Our last example will demonstrate the usefulness of class methods in inheritance. 
We define a class Pet with a method about. This method should give some general class information. 
The class Cat will be inherited both in the subclass Dog and Cat. The method about will be inherited 
as well. We will demonstrate that we will encounter problems, if we define the method about as a normal 
instance method or as a static method. We will start by defining about as an instance method:
"""
class Pet:
    _class_info = "pet animals"
    def about(self):
        print("This class is about " + self._class_info + "!") 

class Dog(Pet):
    _class_info = "men's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()

"""
This may look alright at first at first glance. On second thought we recognize the awful design. 
We had to create instances of the Pet, Dog and Cat classes to be able to ask what the class is about. 
It would be a lot better, if we could just write Pet.about(), Dog.about() and Cat.about() to get the 
previous result. We cannot do this. We will have to write Pet.about(p), Dog.about(d) and Cat.about(c) 
instead.

Now, we will define the method about as a "staticmethod" to show the disadvantage of this approach. 
As we have learned previously in our tutorial, a staticmethod does not have a first parameter with
a reference to an object. So about will have no parameters at all. Due to this, 
we are now capable of calling "about" without the necessity of passing an instance as a parameter, 
i.e. Pet.about(), Dog.about() and Cat.about(). Yet, a problem lurks in the definition of about. 
The only way to access the class info _class_info is putting a class name in front. We arbitrarily 
put in Pet. 
We could have put there Cat or Dog as well. No matter what we do, the solution will not be what we want:
"""

class Pet:
    _class_info = "pet animals"
    @staticmethod
    def about():
        print("This class is about " + Pet._class_info + "!") 

class Dog(Pet):
    _class_info = "men's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()

"""
In other words, we have no way of differenciating between the class Pet and its subclasses Dog and Cat. 
The problem is that the method about does not know that it has been called via the Pet the Dog or the Cat class.

A classmethod is the solution to all our problems. We will decorate about with a classmethod decorator 
instead of a staticmethod decorator:
"""

class Pet:
    _class_info = "pet animals"
    @classmethod
    def about(cls):
        print("This class is about " + cls._class_info + "!") 

class Dog(Pet):
    _class_info = "men's best friends"
class Cat(Pet):
    _class_info = "all kinds of cats"

Pet.about()
Dog.about()
Cat.about()




