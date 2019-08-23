'''
Find the only Pythagorean triplet that adds upto N=1000
'''
import time  # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

number = 1000
# given a < b < c and  a + b + c = number
for a in range(1, int(number / 3)):  # a has to be less than 333 ... a < b < c
    for b in range(a + 1, int(number / 2)):  # b can't be more than the midpoint
        c = number - a - b
        if (a ** 2 + b ** 2 == c ** 2):
            print("Pythagorean triplet product = ", a * b * c, "[[ ", a, b, c, " ]]")

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1000000))
