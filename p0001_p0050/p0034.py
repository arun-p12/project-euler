'''
145 can be represented as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
'''
def digit_factorials(n):
    import math

    sum = 0
    for i in range(10, n):          # upper bound = 2,999,999 ... since 9! = 362,880
        my_list = list(str(i))
        my_fact = 0
        for x in my_list:
            my_fact += math.factorial(int(x))   # add up the factorial of the digits
        if(i == my_fact):
            sum += i
            print("number = ", i, "sum = ", sum)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

digit_factorials(2_999_999)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
