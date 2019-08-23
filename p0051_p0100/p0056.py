'''
For a**b, with a, b < 100 what is the largest value of the digit sum
'''
def powerful_digit_sum():
    max_sum, my_list = 0, [0, 0, 0]
    for a in range(100):
        for b in range(100):
            val = a**b
            digit_sum = sum([int(x) for x in str(val)])
            if(digit_sum > max_sum):
                max_sum = digit_sum
                my_list = [val, a, b]
    print("max sum = ", max_sum, my_list)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

powerful_digit_sum()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))
