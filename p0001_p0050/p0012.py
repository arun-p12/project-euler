'''
Of the triangular numbers 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
28 is the first number with over 5 divisors. Which is the first triangular number to have
over 500 divisors
'''
def highly_divisible_tri_number(number=500):
    import sys
    sys.path.append('../')
    import common as c

    n, len_fact, memo = 1, 0, {}
    while(len_fact < number):
        p, q = n, n + 1
        if(n % 2 == 0): p = int(p/2)
        else: q = int(q/2)

        if p in memo: factors1 = memo[p]
        else:
            factors1 = c.get_factors(p)
            memo[p] = factors1

        if q in memo: factors2 = memo[q]
        else:
            factors2 = c.get_factors(q)
            memo[q] = factors2

        len_fact = len(factors1) * len(factors2)
        n += 1
    #print("hdtn = ", int(n*(n+1)/2), "[[ ", number, len_fact, " ]]")
    sum = int(n*(n-1)/2)        # account for +1 above
    print("Triangle number with more than {} factors = {}   [ factors = {} ]".format(number,
                                                                                     sum,
                                                                                     len_fact))

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

n = 500
highly_divisible_tri_number(n)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))
