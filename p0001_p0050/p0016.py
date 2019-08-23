'''
What is the sum of the digits of the number 2**1000?
'''
def power_digit_sum(base, power):
    # a cheesy brute force
    return(base ** power)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

base, power = 2, 1000
num = power_digit_sum(base, power)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("Power Digit Sum of {} to the power {}  = {}".format(base, power,
                                                           sum([int(x) for x in str(num)]), num))

print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
