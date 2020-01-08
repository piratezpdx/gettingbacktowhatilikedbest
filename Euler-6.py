# https://projecteuler.net/problem=6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def euler6(num):
    # sum_of_numbers = n(n+1)/2
    sum_of_numbers = int(num*(num+1)/2)
    square_of_numbers_summed = 0
    for number in range(1,num+1):
        square_of_numbers_summed += number*number
    print(sum_of_numbers**2 - square_of_numbers_summed)


# invoke as:
# euler6(100)
