'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10
without any remainder. What is the smallest positive number that is evenly divisible by
all of the numbers from 1 to 20?
'''
import time  # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

number, result = 20, 1
for i in (range(1, number+1)):          # the full range of numbers to be checked
    if result % i > 0:
        for j in range(1, number+1):    # the minimum multiplier to make result a full multiple
            if (result * j) % i == 0:
                result *= j
                #print("    match : j = {}, i = {}, result = {}".format(j, i, result))
                break

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("Least common multiple of all numbers upto {} = {}".format(number, result))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
