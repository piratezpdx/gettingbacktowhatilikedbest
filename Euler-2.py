# python3
# By considering the terms in the Fibonacci sequence, find the sum of the even-valued terms.
# assumes user input is reasonable - like not an emoji or whatever

def euler2(limit):
    a = 1 #euler sequence terms
    b = 2 #euler sequence terms
    c = 3 #euler sequence terms, kludge to 3 but can leave as 0. just depends on your thinking.
    total = 2 # account for b term at start
    euler_list = [1,2]
    while c <= limit:
        if c % 2 == 0:
            total += c
        c = a + b
        # euler_list.append(c) # results in an extra term on list at end that is higher than limit. Can avoid with kludge or recursive solution
        a = b
        b = c
    # print(euler_list)
    print(total)
