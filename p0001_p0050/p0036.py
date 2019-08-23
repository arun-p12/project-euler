'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than 1,000,000, which are palindromic in base 10 and base 2.
'''
# check if a string reads the same forward and backward. An easy python thingy
def is_palindrome(num):
    st = str(num)
    if(st == st[::-1]): return(True)
    return(False)

def double_base_palindrome(number):
    palindrome = []
    sum = 0
    # skip even numbers, since they'll end in 0 in base-2
    for num in range(1, number, 2):
        if(is_palindrome(num)):                         # is it a palindrome in base 10
            num_2 = int("{0:b}".format(num))            # a python thingy
            if(is_palindrome(num_2)):                   # palindrome in base 2?
                sum += num
                palindrome.append(str(num) + ":" + str(num_2))
    print("len = ", len(palindrome), "sum = ", sum, palindrome)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

double_base_palindrome(1_000_000)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
