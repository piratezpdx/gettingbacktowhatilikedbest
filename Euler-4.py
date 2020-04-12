'''
euler4
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palin(num):
    '''
    check to see if num is a palindrome; same forward as backwards
    e.g. 123321 or 45654
    '''
    palin = str(num)
    return palin == palin[::-1]



def euler4(num):
    '''
    num is the number of digits in the number expected
    for this specific case of the problem you would invoke this with the number 3
    assumes you enter a natural number
    '''
    found_palins = []

    # first assemble the numbers based on the digit requirements provided
    high_number = '9'*num
    high_number = int(high_number)

    # should probably find at least one within the top 10% of the values
    # commutative property of multiplication, thus b range
    # You could just do 0-999 twice or whatever and sort the list...
    # but that isn't as much fun?

    for mult_a in range(high_number, int(high_number*0.9), -1):
        for mult_b in range(mult_a, int(mult_a*0.9), -1):
            if is_palin(mult_a*mult_b):
                found_palins.append((mult_a*mult_b, mult_a, mult_b))

    print(max(found_palins))
