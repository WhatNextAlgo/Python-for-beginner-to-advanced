definition = """
A computer file is a computer resource for recording data discretely in a
computer storage device. Just as words can be written 
to paper, so can information be written to a computer
file. Files can be edited and transferred through the 
internet on that particular computer system."""

with open(r"Python-for-beginner-to-advanced\File Management\datasets\file_definition.txt","w") as file:
    file.write(definition)


text = open(r"Python-for-beginner-to-advanced\File Management\datasets\file_definition.txt").read()
print(text)