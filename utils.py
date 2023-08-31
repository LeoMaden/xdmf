from typing import Iterable

def array_string(a: Iterable):
    """Returns the elements of `a` in a string separated by spaces
    """
    return " ".join(map(str, a))
