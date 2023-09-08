from typing import Iterable

def array_to_string(a: Iterable) -> str:
    """Returns the elements of `a` in a string separated by spaces
    """
    return " ".join(map(str, a))
