# https://projecteuler.net/problem=7
# what is the 10,001 prime number
# use a sieve 
# The number we are looking for is probably less than 200,000 so this is a just fine solution
# num is the number referred to above

def euler7(num):
    prime_list = [2]
    # we only need odd numbers, we can still sieve by balue of number
    sieve = [x for x in range(3,num,2)]
    for index in range(len(sieve)):
        if sieve[index] != 0:
            prime_list.append(sieve[index])
            update_index = index
            # loop thru and sieve the numbers by adding the value to the index and setting contents to zero
            while update_index < len(sieve):
                sieve[update_index] = 0
                update_index += prime_list[-1]
    print(f"Length of list is {len(prime_list)}")
    if len(prime_list) > 10000:
        print(f"value at 10,001 is {prime_list[10000]}")

# invoke as: euler7(200000)
