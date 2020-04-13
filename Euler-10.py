'''
# Euler 10
# sieve size is the cutoff for the prime list .. as in all numbers below some value x
# sum up all those numbers in the prime list.
# similar execution to euler7

# seem to be needing primes from time to time, so setting this prime finder aside as a tool
# invoke unsing: print(euler10(2000000))
'''

def return_prime_list(sieve_size):
    '''
    # we only need odd numbers in seive, we can still sieve by value of number
    # 2 million in this case since the problem asks for all primes below 2 million
    # can't use enumerate because we want to modify seive on the fly and use
    # results that hae been modified
    '''
    prime_list = [2]
    sieve = list(range(3, sieve_size, 2))
    for index in range(len(sieve)):
        if sieve[index] != 0:
            prime_list.append(sieve[index])
            update_index = index
            # loop thru sieve by adding the value to the index and set contents to zero
            # zero indicates a multiple and thus a non-prime
            while update_index < len(sieve):
                sieve[update_index] = 0
                update_index += prime_list[-1]

    return prime_list


def euler10(threshold):
    '''
    finds the sum of all primes below the threshold value
    '''
    return sum(return_prime_list(threshold))
