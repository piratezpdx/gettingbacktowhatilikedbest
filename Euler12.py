# result is used to decrease number of computations required to come up with a list of factors
def find_factors(number):
    counter = 0
    result = number
    factors = set() 
    keep_looking = True

    while keep_looking:
        counter += 1
        if counter > result:
            keep_looking = False
        if number % counter == 0:
            result = int(number/counter)
            factors.add(result)
            factors.add(counter)

    return factors



# What is the value of the first triangle number to have over five hundred divisors?
# thought about using a pseudo search and traverse method, but couldn't guarantee that a random number would
# be truly representative


def euler12(number_of_divisors):
    triangle_number = 1
    triangle_counter = 1
    triangle_divisors = set()  # given in problem as: 1

    while len(triangle_divisors) < number_of_divisors:
        triangle_counter += 1
        triangle_number += triangle_counter
        triangle_divisors = find_factors(triangle_number)
        if triangle_counter % 1000 == 0: # show progress
            print(".", end = ' ')
    print(f"\nNumber of divisors: {len(triangle_divisors)}, triangle number: {triangle_number}, triangle counter: {triangle_counter}")

euler12(501)
