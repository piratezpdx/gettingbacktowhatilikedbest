# basically an increased version of prime_find_factors that finds prime factors and
# then ...
def find_factors(num):
    factors_found = set()

    found = False
    for denom in range(2,num):
        if num % denom == 0:
            found = True
            factors_found = (find_factors(int(num/denom)))
            factors_found.add(denom)
            break

    if not found:
        # factors_found.add(num) - from finding primes
        factors_found.add(1) # include 1 as a factor per the problem specs

    # ... when done finding primes, look for additional factors based on primes found
    factors_found.add(num)
    additional_factors = [ int(num/factor) for factor in factors_found ]
    for factor in additional_factors:
        factors_found.add(factor)
    return factors_found



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

# euler12(501)


def unit_test_for_find_factors():
    if find_factors(16) != {1, 2, 4, 8, 16}:
        print(f'find_factors(16) yields: {find_factors(16)}')
    if find_factors(99) != {1, 3, 9, 11, 33, 99}:
        print(f'find_factors(99) yields: {find_factors(99)}')
    if find_factors(12) != {1, 2, 3, 4, 6, 12}:
        print(f'find_factors(12) yields: {find_factors(12)}')
    if find_factors(15) != {1, 3, 5, 15}:
        print(f'find_factors(15) yields: {find_factors(15)}')
    if find_factors(32) != {1, 2, 4, 8, 16, 32}:
        print(f'find_factors(32) yields: {find_factors(32)}')
    if find_factors(24) != {1, 2, 3, 4, 6, 8, 12, 24}:
        print(f'find_factors(24) yields: {find_factors(24)}')
    if find_factors(144) != {1,2,3,4,6,8,9,12,16,18,24,36,48,72,144}:
        print(f'find_factors(24) yields: {find_factors(144)}')
    if find_factors(10) != {1, 2, 5, 10}:
        print(f'find_factors(10) yields: {find_factors(10)}')
