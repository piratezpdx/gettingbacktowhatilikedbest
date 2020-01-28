# sieve size is the cutoff for the prime list .. as in all numbers below some value x
# sum up all those numbers in the prime list.
# similar execution to euler7

# we seem to be needing primes from time to time, so I am setting this prime finder aside as a future tool
def return_prime_list(sieve_size):
    prime_list = [2]
    # we only need odd numbers, we can still sieve by value of number
    # 2 million since the problem asks for all primes below 2 million
    sieve = [x for x in range(3,sieve_size,2)]
    for index in range(len(sieve)):
        if sieve[index] != 0:
            prime_list.append(sieve[index])
            update_index = index
            # loop thru and sieve the numbers by adding the value to the index and setting contents to zero
            while update_index < len(sieve):
                sieve[update_index] = 0
                update_index += prime_list[-1]

    return prime_list

def euler10(max_prime):
    return sum(return_prime_list(max_prime))

# print(euler10(2000000))
