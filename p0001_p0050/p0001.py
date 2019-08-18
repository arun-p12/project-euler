'''
Given: Find the sum of all the multiples of 3 or 5 below 1000.
Extension: sum of all multiples of a arbitrary set of numbers,
# with a user specified start and stop.
E.g. sum of all multiples of 2, 4, 5, and 11 upto 100
'''
def p0001_multiples_sum(**kwargs):
    start, stop, num, verbose = 0, 1000, [3, 5], 0
    if 'start' in kwargs: start = kwargs['start']
    if 'stop' in kwargs: stop = kwargs['stop']
    if 'num' in kwargs: num = kwargs['num']
    if 'verbose'in kwargs: verbose = 1

    import time     # get a sense of the time taken
    t = time.time()         # get time just before the main routine

    ########## the main routine #############

    result = set()
    for n in num:
        for i in range(start, stop, n):
            result.add(i)
        if(verbose): print("set :", n, " :: ", result)

    ########## end of main routine ###########

    t = time.time() - t             # and now, after the routine
    print("Sum of multiples of {} upto {} = {}".format(num, stop, sum(result)))
    print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t*1000, t*100000))

p0001_multiples_sum()
#p0001_multiples_sum(num=[3, 5], stop=15, verbose=1)