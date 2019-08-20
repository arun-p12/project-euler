'''
192 x 1 = 192 ; 192 x 2 = 384 ; 192 x 3 576
str(192) + str(384) + str(576) = '192384576' which is a 1-9 pandigital number.

What is the  largest 1 to 9 pandigital 9-digit number that can be formed as the
concatenated product of an integer with (2, ... , n) digits?
Essentially n > 1 to rule out 918273645  (formed by 9x1 9x2 9x3 ...)
'''
'''
Cycle thru each number, get the multiples, and keep appending the string of numbers.
When length of the string goes above 9, move onto the next number.
If the length of the string is 9, check if it is pandigital. If yes, check if it is maximum
'''
def pandigital_multiple():
    target = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    max_str = ""

    #for x in range(9876, 0, -1):        # start from top, and decrement
    for x in range(1, 9877):
        i, pand_len = 1, 0
        pand_list = []                  # sort and test against target
        pand_str = ""                   # this is our actual string
        while (pand_len < 9):
            next_num = x * i           # take each number, and multiply by the next i
            pand_str += str(next_num)
            for c in str(next_num):     # append new number to our list
                pand_list.append(int(c))
            pand_len = len(pand_list)
            i += 1
        #print("test : ", x, pand_len, i, pand_list, pand_str, pand_cont)
        if pand_len == 9:
            pand_list.sort()
            if pand_list == target:
                if(pand_str > max_str): max_str = pand_str
                print("start_num = ", "{:4d}".format(x),
                      "mult_upto = ", "{:1d}".format(i - 1),
                      "result = ", "{:10s}".format(pand_str),
                      "max = ", "{:10s}".format(max_str))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

pandigital_multiple()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))