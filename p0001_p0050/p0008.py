'''
the thirteen adjacent digits in the 1000-digit number that have the greatest product.
What is the value of this product?
'''
import time  # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############
file = './p0008_series.txt'
number = 13

import re
num_list = [line.strip().split(',') for line in open(file, "r").readlines()]

n_list = []
num_str = str(num_list)
num_str = re.sub('["\[\]\', ]', '', num_str)     # strip off characters: "[], '
n_list = list(num_str)

max = 0
n_dict = {}
for i in range(0, len(n_list)):
    # save the list of <number> consequtive numbers
    n_dict[i % number] = int(n_list[i])         # could have been done with a list too
    product = 1                                 # initialize product

    # find the product of the consequtive numbers
    if(number - 1 in n_dict):                   # start only after the list is filled
        for key in n_dict:
            product *= n_dict[key]
        if(product > max): max = product
    i += 1

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("Largest value of product of {} consequtive digits = {}".format(number, max))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1000000))
