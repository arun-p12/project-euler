'''
1634 = 1**4 + 6**4 + 3**4 + 4**4
What is the sum of ALL numbers that can be represented as the sum of the 5th power of its digits

Since 9**5 = 59,049, a
   - 3-digit number can result upto 177,147,    (999)
   - 4-digit number can result upto 236,196,    (9,999)
   - 5-digit number can result upto 295,245,    (99,999)
   - 6-digit number can result upto 354,294     (999,999)
Thus, we know the upper bound of the solution is a 6-digit number.
Futher filteration helps set the upper bound to 399,999  (sum = 295488)
'''
def digit_nth_power(power, number=399999):
    results = []
    tot_sum = 0
    for i in range(2, number):          # iterate thru each number
        sum = 0                         # local sum
        for x in str(i):
            sum += int(x) ** power      # get the digit, find its power, append to local sum
        if(sum == i):                   # if match, save number, and update result sum
            results.append(i)
            tot_sum += i
    print("result = ", results, "sum = ", tot_sum)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

digit_nth_power(5)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))