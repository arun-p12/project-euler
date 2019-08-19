'''
Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''

import time  # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

number, power = 100, 2
pow_sum = sum(range(1, number+1)) ** power
sum_pow = sum([x ** power for x in range(1, number+1)])

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("pow_sum_diff = {}  [[ power_sum = {}, sum_power = {} ]]".format((pow_sum - sum_pow),
                                                                       pow_sum, sum_pow))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))
