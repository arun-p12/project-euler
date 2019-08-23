'''
For values of n <= 100, how many combinations of nCr produces a value greater than 1,000,000
'''


def combinatoric_selection():
    def ncr(n, r):
        import math
        return (math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))

    '''
    nCr values for a Pascal's triangle ... 1; 1 1; 1 2 1; 1 3 3 1; 1 4 6 4 1; 1 5 10 10 5 1; etc
    Thus nCr = (n-1)C(r-1) + (n-1)Cr

    Code might look neat ... but, slow as hell ... due to exponential increase in # of calls
    '''

    def ncr_recursive(n, r):
        if ((r == 0) or (n == 0)): return (1)
        return (ncr_recursive(n - 1, r - 1) + ncr_recursive(n - 1, r))

    target, result = 1000000, {}
    for n in range(101):
        for r in range(n):
            val = ncr(n, r)
            # print(n, r, val)
            if (val > target): result[str(n) + "C" + str(r)] = val
    print("count = ", len(result))

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

combinatoric_selection()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
