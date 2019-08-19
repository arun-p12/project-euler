'''
Of the triangular numbers 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
28 is the first number with over 5 divisors. Which is the first triangular number to have
over 500 divisors
'''
def highly_divisible_tri_number(number=500):
    import sys
    sys.path.append('../')
    import common as c

    sum, i, len_fact, factors = 0, 0, 0, []
    while(len_fact < number):
        i   += 1
        sum += i
        factors = c.get_factors(sum)
        len_fact = len(factors)
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
