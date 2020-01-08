# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# algorithm:
# come up with a list of numbers to multiply: this list should be a subset of range(2,21)
# it of course has all primes on it in the range, and those primes are duplicated as necessary ..
# by way of example, if our range was the following numbers: 2,4,8,10... 80 meets the criteria, but 40 is sufficient.
# so extract all the factors from the list and then multiply them all together, we do this by modifying the
# factor list as we go, both decreasing the length and by reducing the numbers in the list.

def euler5(num):
    answer = 1
    factor_list = [x for x in range(2,num+1)]
    multiplier_list = []
    while len(factor_list) > 0:
        multiplier_list.append(factor_list.pop(0))
        factor_list = [int(x/multiplier_list[-1]) if x % multiplier_list[-1] == 0 else x for x in factor_list]

    for number in multiplier_list:
        answer *= number
    print(answer)

#invoke as:
# euler5(20)
