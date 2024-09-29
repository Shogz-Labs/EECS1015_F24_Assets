import doctest

def generate_triangle(height: int) -> str:    
    r"""
    >>> generate_triangle(-1)
    Traceback (most recent call last):
    AssertionError: Negative height is not allowed.
    >>> generate_triangle(3)
    '*\n**\n***'
    >>> generate_triangle(5)
    '*\n**\n***\n****\n*****'
    """
    assert height >= 0, "Negative height is not allowed."
    triangle = '\n'.join('*' * (i + 1) for i in range(height))
    return triangle

if __name__ == '__main__':
    doctest.testmod(verbose=True)


