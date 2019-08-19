'''
If n → n/2 (when n is even) and n → 3n + 1 (when n is odd), then we get the sequence
(if we start with 13) 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

Which starting number, under one million, produces the longest chain?
'''
def longest_collatz(number=1000000):
    cache = {1: 1}

    def my_collatz(n):
        if n not in cache:
            cache[n] = my_collatz(3 * n + 1 if n % 2 else n / 2) + 1
        return cache[n]  # Length of Collatz Chain

    # for i in range(1, number+1)  run my_collatz(i) and get the maximum
    print("Longest Collatz = ", max(range(1, number), key=my_collatz))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

longest_collatz()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))
