'''
49/98 = 1/2 ... which is the same as 4/8, if we cancel off the 9.
There are 4 such 2-digit examples (if we ignore trivial examples such as 30/50 and 12/12)

Take three digits A, B, and C. Now check AB/BC and AB/CB. Check if this fraction equals A/C
Examples:
    . digits are 1, 1, and 2        :: 11/12 or 11/21  must equal 1/2 (false)
    . digits 2, 3, and 3            :: 23/33           must equal 2/3 (false)
    . digits 1, 6, and 4            :: 16/64 or 16/46  must equal 1/4 (true)
'''
def digit_cancelling_fractions():
    product = 1
    for d1 in range(1, 10):
        for d2 in range(d1, 10):            # originally had range(1, 10)
            nn = int(str(d1) + str(d2))
            for d3 in range(d1+1, 10):      # originally had range(1, 10)
                for i in [(int(str(d2) + str(d3))), (int(str(d3) + str(d2)))]:
                    if((nn/i == d1/d3)):    # originally also checked if(nn != i)
                        product *= d1/d3
                        print(d1, d2, d3, " :: ", nn, i, " :: ", nn/i)
    print("denominator = ", 1/product)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

digit_cancelling_fractions()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
