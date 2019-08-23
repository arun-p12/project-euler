'''
The 12th digit of an irrational decimal fraction 0.123456789101112131415161718192021... is 1
What is the product of the digits positioned at the powers of 10, upto 1000000?
'''
def champernownes_constant():
    #initialize a counter, positions we are interested in, final result, array of digits, ...
    i, pos, product, string, my_list = 1, 1, 1, '', []
    while(len(string) <= 1000000):
        string += str(i)
        if((i % pos) == 0):         # is this a position we're interested in?
            my_list.append(string[pos-1])       # account for pos = 1 is really index-0
            product *= int(string[pos-1])
            pos *= 10
        i += 1
    print("product = ", product, my_list)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

champernownes_constant()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
