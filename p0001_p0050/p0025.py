'''
In a Fibonacci series 1, 1, 2, 3, 5, 8, ... the first 2-digit number (13) is the 7th term.
Likewise the first 3-digit number (144) is the 12th term.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
'''
def n_digit_fibonacci(number):
    digits = 1
    fibonacci = [1, 1]
    while(digits < number):
        fibonacci.append(fibonacci[-1] + fibonacci[-2]) # next term = sum of last two terms
        digits = len(str(fibonacci[-1]))                # how many digits in the new term?
        if(digits >= number):                           # is it the required length
            print("fibonacci = ", len(fibonacci))
            return(0)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

number = 1000
n_digit_fibonacci(number)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))