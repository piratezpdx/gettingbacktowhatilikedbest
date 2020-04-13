"""
Euler 2 - python3.8
By considering the terms in the Fibonacci sequence, find the sum of the even-valued terms.
assumes user input is reasonable - like not an emoji or whatever
"""

def euler2(limit):
    """
    limit is what number to stop the sequence at or below
    """
    
    first = 1 #euler sequence terms
    second = 2 #euler sequence terms
    next_term = 3 #euler sequence terms, kludge to 3 but can leave as 0
    total = 2 # account for b term at start
    # euler_list = [1, 2]
    while next_term <= limit:
        if next_term % 2 == 0:
            total += next_term
        next_term = first + second
        first = second
        second = next_term
    # print(euler_list)
    # print(sum(filter(lambda x: x%2 == 0,euler_list[:-1])))
    # print(total)
    return total
