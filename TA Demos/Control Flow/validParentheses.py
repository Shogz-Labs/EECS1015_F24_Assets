import doctest

"""
This is one simple example of implementing Valid Parentheses. 
Try it out for yourself. 

Consider the following in your attempt:
    1) How can the time complexity be further improved?
    2) How can the space complexity be improved?
    3) Implement some more tests 
    4) What would the flowchart of your algorithm look like?  
"""

def isValid(s):
    """
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

    ----- Constraints -----    
    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

    >>> isValid('()')
    True
    >>> isValid('()[]{}')
    True
    >>> isValid('(])')
    False
    >>> isValid('([])')
    True
    >>> isValid(']')
    False
    """

    stack = []

    expected = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }

    for bracket in s:
        # Case 1: Read an Opening Bracket
        if bracket in '([{':
            stack.append(bracket)
        # Case 2: Read a Closing Bracket
        else:
            if len(stack) == 0 or stack.pop() != expected[bracket]:
                return False
    return len(stack) == 0 





            



doctest.testmod()