'''
How many distinct paths are there to traverse from the top left corner to the bottom right
corner of a nxn square. All movements are restricted either to the right or down by one unit
E.g. A 1x1 grid has 2 paths. A 2x2 grid would have 6 paths.
'''
def lattice_path(number=20):
    # initialize the two dimensional matrix, starting with the zeroth cells
    lattice = {}
    for j in range(0, number+1):
        lattice[j] = {}
        lattice[0][j] = 1           # the top edge
        lattice[j][0] = 1           # the left edge

    # now do all the other cells... initialize them to zero
    for i in range(1, number+1):
        for j in range(1, number+1):
            lattice[i][j] = 0

    for i in range(1, number + 1):
        for j in range(1, number + 1):
            lattice[i][j] = lattice[i - 1][j] + lattice[i][j-1]
    print("lattice paths = ", lattice[number][number])

# if one knows a bit of math, the programming can be dramatically simplified!
# for an NxM grid, the paths are   (N+M)! / (N! * M!)
def lattice_path_2(number=20):
    from math import factorial

    def grid(n, m):
        return factorial(n + m) / (factorial(n) * factorial(m))
    print("lattice paths  = ", int(grid(number, number)))



import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

lattice_path()
#lattice_path_2()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t*1_000_000))
