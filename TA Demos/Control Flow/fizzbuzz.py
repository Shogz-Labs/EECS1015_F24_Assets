import doctest
"""
This is one simple example of implementing FizzBuzz. 
Try it out for yourself. 

Consider the following in your attempt:
    1) How can the time complexity be further improved?
    2) How can the space complexity be improved?
    3) Can the problem be done by only using if-statements? (no elif, no else). 
    4) Implement some more tests 
    5) What would the flowchart of your algorithm look like?  
"""

def fizzBuzz(n: int) -> list:
    """
    Given an integer n, return a string array answer (1-indexed) where:
        i) answer[i] == 'FizzBuzz' if i is divisible by 3 and 5 
        ii) answer[i] == 'Fizz' if i is divisible by 3 
        iii) answer[i] == 'Buzz' if i is divisible by 5
        iv) answer[i] = str(i) if none of the conditions are true
    >>> fizzBuzz(3)
    ['1', '2', 'Fizz']
    >>> fizzBuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    >>> fizzBuzz(15)
    ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    >>> fizzBuzz('tacos')
    Traceback (most recent call last):
    ...
    AssertionError: n must be an integer
    >>> fizzBuzz(10 ** 5)
    Traceback (most recent call last):
    ...
    AssertionError: n is out of bounds
    """
    assert type(n) == int, 'n must be an integer'
    assert 1 <= n <= 10 ** 4, 'n is out of bounds'
    sol = []
    for i in range(1, n + 1):
        divByThree = i % 3 == 0 
        divByFive = i % 5 == 0
        if divByThree and divByFive:
            sol.append('FizzBuzz')
        elif divByThree:
            sol.append('Fizz')
        elif divByFive:
            sol.append('Buzz')
        else:
            sol.append(str(i))
    return sol

doctest.testmod()