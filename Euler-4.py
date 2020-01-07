# https://projecteuler.net/problem=4
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palin(num):
    palin = str(num)
    return palin == palin[::-1]


# num is the number of digits in the number expected
# for this specific case of the problem you would invoke this with the number 3
# assumes you enter a natural number ... generally I am writing these with the
# expectation that you are going to play nice

def euler4(num):
    # assemble the numbers based on the digit requirements provided
    high_number = '9'*num
    high_number = int(high_number)

    found_palins=[]

    # should probably find at least one within the top 10% of the values
    # commutative property of multiplication, thus b range
    # I guess you could just do 0-999 twice or whatever and sort the list...
    # but that isn't as much fun?
    
    for a in range(high_number,int(high_number*0.9),-1):
        for b in range(a,int(a*0.9),-1):
            if is_palin(a*b):
                found_palins.append((a*b,a,b))
                
    print(max(found_palins))
