'''
5! = 120, and the sum of the digits of 5! is 3. What is the sum of the digits of 100!
'''
def factorial_digit_sum(number=100):
    from operator import mul
    from functools import reduce

    product = reduce(lambda x, y: x * y, range(1, number + 1))
    print("Sum of digits of {}! = {}".format(number, sum([int(x) for x in str(product)])))

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

factorial_digit_sum()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
