"""
euler 3
"""

def prime_factor_finder(num):
    """
    recursively find prime factors of a number
    """
    factors_found = set()
    found = False
    for denom in range(2, num):
        if num % denom == 0:
            found = True
            factors_found = (prime_factor_finder(int(num/denom)))
            factors_found.add(denom)
            break

    if not found:
        factors_found.add(num)

    return factors_found

def euler3():
    """wrapper for prime_factor_finder which will be useful elsewhere probably"""
    return max(prime_factor_finder(600851475143))
