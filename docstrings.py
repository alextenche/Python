def does_something(arg):
    """Takes one argument and does something, based on type
    If arg is an number, returns arg + 10
    If arg is a string, returns args * 3
    """
    if isinstance(arg, (int, float)):
        return arg + 10
    elif isinstance(arg, str):
        return str * 3
    else:
        raise TypeError("does_something only takes ints, floats, and strings")

# help(docstrings.does_something)
