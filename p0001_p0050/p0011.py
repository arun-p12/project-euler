'''
the greatest product of N adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
'''
def largest_product_grid(number=4):
    from functools import reduce
    # a flat list ... with each member stored as integer
    # x = [int(num) for line in open('./grid11.txt', "r").readlines() for num in line.strip().split()]

    # list of lists ..... each line as a list.. but, each number stored as a string
    x = [line.strip().split() for line in open('./p0011_grid.txt', "r").readlines()]

    # list of lists ... with l[i][j] stored as integer
    x = [[int(num) for num in list] for list in x]
    # print(x)

    max_score = 0
    grid_rows = len(x)
    grid_cols = len(x[grid_rows - 1])  # assuming each row has the same # of cols

    for row in range(0, grid_rows):
        for col in range(0, grid_cols):
            # initialize the product grid
            # num_dict = {'right': t_list, 'down': t_list, 'diag_r': t_list, 'diag_l': t_list}
            num_dict = {'right': [], 'down': [], 'diag_r': [], 'diag_l': []}
            for i in range(0, number):
                # setup the series of numbers to the right :: advance col
                if (col + i >= grid_cols): num_dict['right'].append(0)
                else:
                    num_dict['right'].append(x[row][col + i])
                # print("right  = ", num_dict['right'], i, row, col)

                # setup the series of numbers down :: advance row
                if (row + i >= grid_rows): num_dict['down'].append(0)
                else:
                    num_dict['down'].append(x[row + i][col])
                # print("down   = ", num_dict['down'], i, row, col)

                # setup the diagonal row (right) :: advance row and column
                if ((col + i >= grid_cols) | (row + i >= grid_rows)):
                    num_dict['diag_r'].append(0)
                else:
                    num_dict['diag_r'].append(x[row + i][col + i])
                # print("diag_r = ", num_dict['diag_r'], i, row, col)

                # setup the diagonal row (left) :: advance row and decrement column
                if ((col - i < 0) | (row + i >= grid_rows)):
                    num_dict['diag_l'].append(0)
                else:
                    num_dict['diag_l'].append(x[row + i][col - i])
                # print("diag_l = ", num_dict['diag_l'], i, row, col)

                # print("dict = ", num_dict)
                right = reduce(lambda x, y: x * y, num_dict['right'])
                down = reduce(lambda x, y: x * y, num_dict['down'])
                diag_r = reduce(lambda x, y: x * y, num_dict['diag_r'])
                diag_l = reduce(lambda x, y: x * y, num_dict['diag_l'])

            #print("lpg = ", right, down, diag_r, diag_l)
            max_score = max(max_score, right, down, diag_r, diag_l)
    return(max_score)

import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############
n = 4
max_score = largest_product_grid()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("Largest product of {} numbers in the grid = {}".format(n, max_score))
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 1_000_000))

