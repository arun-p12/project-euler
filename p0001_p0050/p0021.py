'''
proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110. It adds upto 284
The proper divisors of 284 are 1, 2, 4, 71 and 142; which adds upto 220. such numbers are
called amicable numbers. What is the sum of all the amicable numbers under 10000?
'''

def amicable_numbers(number=10000):
    import sys
    sys.path.append('../')
    import common as c

    def factors_sum(x):
        return(sum(c.get_factors(x)) - x)    # the number itself is not counted as a divisor


    dict, a_sum = {}, 0
    for x in range(1, number+1):
        dict[x] = factors_sum(x)
        y = dict[x]
        dict[y] = factors_sum(y)
        if((dict[x] != x) & ((dict[y]) == x)):    # ignoring where the sum of divisors is the number itself
            #print("amicable = ", x, y, get_factors(x), get_factors(y))
            print("  is amicable = ", x, y)
            a_sum += x
    return(a_sum)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

number = 10000
amicable = amicable_numbers(number)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("Sum of all amicable numbers under {} = {}".format(number, amicable))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))