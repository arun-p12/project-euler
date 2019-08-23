'''
given a file with several 50-digit numbers, calculate the first ten digits of the sum of the #s
'''
def large_sum(number=10):
    file = './p0013_number.txt'
    x = [int(num) for line in open(file, "r").readlines()
         for num in line.strip().split()]
    x_sum = list(str(sum(x)))
    first_num = ''
    for n in range(0, number): first_num += x_sum[n]
    print("First {} digits of {} = {}".format(number, sum(x), first_num))

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

large_sum()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
