# https://projecteuler.net/problem=9
# find the product of a*b*c for a,b,c for which:
# a + b + c = 1000 and a^2 + b^2 = c^2
# using brute force which is slow
# making some broad assumptions about the numbers

def euler9():
    the_numbers=(0,0,0)
    exit = False
    for a in range(0,500):
        if exit:
            break
        for b in range(0,500):
            if exit:
                break
            for c in range(200,700):
                if (a + b + c == 1000) and (a*a + b*b == c*c) and not b == c and not exit:
                    the_numbers=(a,b,c)
                    exit = True

    print(f"a: {the_numbers[0]}, b: {the_numbers[1]}, c: {the_numbers[2]}")
    return the_numbers[0]*the_numbers[1]* the_numbers[2]

# invoke using: print(euler9())
