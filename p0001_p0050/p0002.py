'''
Given:  find the sum of the even-valued Fibonacci terms not exceeding 4,000,000
Extension: sum of all multiples of a arbitrary set of numbers,
# with a user specified start and stop.
E.g. sum of all multiples of 2, 4, 5, and 11 upto 100
'''
def p0002_even_fibonacci(**kwargs):
    start, stop, verbose = 0, 4000000, 0
    if 'start' in kwargs: start = kwargs['start']
    if 'stop' in kwargs: stop = kwargs['stop']
    if 'verbose'in kwargs: verbose = 1

    import time     # get a sense of the time taken
    t = time.time()         # get time just before the main routine

    ########## the main routine #############

    # 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    # pattern = O, O, E, O, O, E, O, O, E, ...   thus, advance x and y by two numbers
    # evens = 2, 8, 34, 144, ...     odds = 1, 1, 3, 5, 13, 21, 55, 89
    x = y = 1
    sum = 0
    while (sum < stop):
        if(verbose): print("  current sum =", sum, " next even = ", x+y)
        sum += (x + y)                    # this is the even Fibonacci
        x, y = (x + 2*y), (2*x + 3*y)     # these are the odd ones

    ########## end of main routine ###########

    t = time.time() - t             # and now, after the routine
    print("Sum of even Fibonacci upto {} = {}".format(stop, sum))
    print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t*1000, t*100000))

p0002_even_fibonacci(verbose=1)