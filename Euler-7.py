'''
Euler 7
what is the 10,001 prime number
invoke as: euler7(200000)
'''

def euler7(num):
    '''
    algorithm: use a sieve
    num is the highest number of the sieve that we build
    The number is probably less than 200,000 so this is a reasonable solution
    '''
    prime_list = [2]
    # we only need odd numbers, we can still sieve by value of number
    sieve = [x for x in range(3, num, 2)]

    for index in range(len(sieve)):
        # we can't use enumerate because we are modifying the sieve on the fly
        if sieve[index] != 0:
            prime_list.append(sieve[index])
            update_index = index
            # loop thru sieve by adding the value to the index and set contents to zero
            # indicating that the number was a multiple and not prime
            while update_index < len(sieve):
                sieve[update_index] = 0
                update_index += prime_list[-1]
    print(f"Length of list is {len(prime_list)}")
    if len(prime_list) > 10000:
        print(f"value at 10,001 is {prime_list[10000]}")
    else:
        print(f"Value not found, the sieve needs to be larger than {num}")
