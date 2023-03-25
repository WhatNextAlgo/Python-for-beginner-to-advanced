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

