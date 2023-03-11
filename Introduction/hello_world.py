import sys
def argument(args):
    if len(args) > 1:
        return "Hello, " + ", ".join(args[1:])
    return "Hello everyone!"

if __name__ == "__main__":
    print(argument(sys.argv))
    

