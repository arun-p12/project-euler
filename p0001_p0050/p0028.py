'''
What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed by starting
at the center and moving in a clockwise direction?
'''

'''
Starting from the center, the diagonals are the four corners of a sqaure, and increment by 2n.
The center point is a 1x1 square, the next is a 2x2, and so on. Thus, the corners of a 4x4 
square would increment by 2x4 = 8, and the diagonals would follow a pattern of
1,    3,5,7,9,    13,17,21,25,       31,37,43,49,     57,65,73,81, ... 
'''
def spiral_diagonals(number):
    sum, pointer, adder = 1, 1, 0
    for i in range(1, int(number / 2) + 1):     # number of steps from center ..
        adder += 2                              # becomes 2, 4, 6, 8, ... with each iteration
        for x in range(1, 5):                   # the four corners of the square
            pointer += adder
            sum += pointer
    print("sum = ", sum)


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

spiral_diagonals(1001)

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))