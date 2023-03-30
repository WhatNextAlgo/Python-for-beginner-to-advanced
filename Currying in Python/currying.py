"""
General Idea
In mathematics and computer science, currying is the technique of breaking down the evaluation 
of a function that takes multiple arguments into evaluating a sequence of single-argument functions.
Currying is also used in theoretical computer science, 
because it is often easier to transform multiple argument models into single argument models.
"""
#Composition of Functions

def compose(g, f):
    def h(x):
        return g(f(x))
    return h

def celsius2fahrenheit(t):
    return 1.8 * t + 32
def readjust(t):
    return 0.9 * t - 0.5
convert = compose(readjust, celsius2fahrenheit)
print(convert(10), celsius2fahrenheit(10))

convert2 = compose(celsius2fahrenheit, readjust)
print(convert2(10), celsius2fahrenheit(10))


#"compose" with Arbitrary Arguments
def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h
def BMI(weight, height):
    return weight / height**2
def evaluate_BMI(bmi):
    if bmi < 15:
        return "Very severely underweight"
    elif bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal (healthy weight)"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I (Moderately obese)"
    elif bmi < 40:
        return "Obese Class II (Severely obese)"
    else:
        return "Obese Class III (Very severely obese)"
f = compose(evaluate_BMI, BMI)
again = "y"
while again == "y":
    weight = float(input("weight (kg) "))
    height = float(input("height (m) "))
    print(f(weight, height))
    again = input("Another run? (y/n)")


def arimean(*args):
    return sum(args) / len(args)
def curry(func):
    # to keep the name of the curried function:
    curry.__curried_func_name__ = func.__name__
    f_args, f_kwargs = [], {}
    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            f_args += args
            f_kwargs.update(kwargs)
            return f
        else:
            result = func(*f_args, *f_kwargs)
            f_args, f_kwargs = [], {}
            return result
    return f
curried_arimean = curry(arimean)
curried_arimean(2)(5)(9)(4, 5)
# it will keep on currying:
curried_arimean(5, 9)
print(curried_arimean())
# calculating the arithmetic mean of 3, 4, and 7
print(curried_arimean(3)(4)(7)())
# calculating the arithmetic mean of 4, 3, and 7
print(curried_arimean(4)(3, 7)())

#Let's compare it with the result of the original arimean function:


print(arimean(2, 5, 9, 4, 5, 5, 9))
print(arimean(3, 4, 7))
print(arimean(4, 3, 7))


#Including some prints might help to understand what's going on:


def arimean(*args):
    return sum(args) / len(args)
def curry(func):
    # to keep the name of the curried function:
    curry.__curried_func_name__ = func.__name__
    f_args, f_kwargs = [], {}
    def f(*args, **kwargs):
        nonlocal f_args, f_kwargs
        if args or kwargs:
            print("Calling curried function with:")
            print("args: ", args, "kwargs: ", kwargs)
            f_args += args
            f_kwargs.update(kwargs)
            print("Currying the values:")
            print("f_args: ", f_args)
            print("f_kwargs:", f_kwargs)
            return f
        else:
            print("Calling " + curry.__curried_func_name__ + " with:")
            print(f_args, f_kwargs)
            result = func(*f_args, *f_kwargs)
            f_args, f_kwargs = [], {}
            return result
    return f
curried_arimean = curry(arimean)
curried_arimean(2)(5)(9)(4, 5)
# it will keep on currying:
curried_arimean(5, 9)
print(curried_arimean())