'''
1/6 = 0.166666... with a single digit repeating ; 1/7 = 0.(142857) with 6 digits repeating
Find the value of d < 1000 for which 1/d contains the longest recurring cycle
'''
def reciprocal_cycles(number):
    maxlen_num = 0          # the number that produces the longest repeat set
    maxrep_len = 0          # the length of the repeat set
    for i in range(1, number + 1):
        # initialize a few variables for long division
        numer = 1
        quo_list = []  # list of quotients
        rem_list = []  # list of remainders
        repeater = 0  # number that gets repeated (using remainder list)
        repeat_len = 0  # length of the repeat sequence
        reptend = 0  # Is the number a reptend prime   [repeat len for 1/n is (n-1)]
        while (numer % i):      # we'll keep updating the numerator with the remainder
            # get the quotient and remainder
            if (numer < i): numer *= 10
            quo = int(numer / i)
            rem = numer % i
            # print(numer, i, quo, rem)
            if rem:  # don't have to worry if no remainder left (fully divisible)
                if rem in rem_list:  # have we seen the remainder before?
                    repeater = quo_list
                    repeat_len = len(rem_list) - rem_list.index(rem)
                    # is this number the one with the longest repeater pattern?
                    if (repeat_len > maxrep_len):   # we have a new maximum
                        maxlen_num = i
                        maxrep_len = repeat_len
                        # is this number a reptend prime? Checking this just for fun
                        if (i == repeat_len + 1): reptend = 1
                        #print("num=", i, "reptend=", reptend, "repeater=", repeater, "repeat_len=", repeat_len)
                    break
                numer = rem
            quo_list.append(quo)
            rem_list.append(rem)
    print("Longest repeating seq ... ", "num =", maxlen_num, "repeat_len =", maxrep_len)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

number = 1000
reciprocal_cycles(number)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))