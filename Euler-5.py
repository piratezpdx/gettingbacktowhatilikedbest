'''
Euler 5: What is the smallest positive number that is evenly divisible by all of the numbers
from 1 to 20?
invoke as:
euler5(20)
'''

def euler5(num):
    '''
    algorithm:
    come up with a list of numbers to multiply: this list should be a subset of
    range(2,21) it of course has all primes on it in the range, and those primes are
    duplicated as necessary ..  by way of example, if our range was the following
    numbers: 2,4,8,10... 80 meets the criteria, but 40 is sufficient.  So extract all
    the factors from the list and then multiply them all together, we do this by modifying the
    factor list as we go, both decreasing the length and by reducing the numbers in the list.
    '''
    answer = 1
    factors = [x for x in range(2, num+1)]
    multipliers = []
    while len(factors) > 0:
        multipliers.append(factors.pop(0))
        factors = [int(x/multipliers[-1]) if x % multipliers[-1] == 0 else x for x in factors]

    for number in multipliers:
        answer *= number
    print(answer)
