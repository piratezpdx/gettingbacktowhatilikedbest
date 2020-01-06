# What is the largest prime factor of the number 600851475143

def prime_factor_finder(num):
    # print(num)
    factors_found = set()
    found = False
    for denom in range(2,num):
        if num % denom == 0:
            found = True
            factors_found = (prime_factor_finder(int(num/denom)))
            factors_found.add(denom)
            break

    if not found:
        factors_found.add(num)

    return factors_found
