'''
Navigating the path from top to bottom of a given triangle ... find the path that
maximizes the sum of the numbers traversed through.
'''
def max_path_sum(file='./p0018_path.txt'):
    # read each line, and store the numbers in the line, in an array.
    # e.g. [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    numbers = [line.strip().split() for line in open(file, "r").readlines()]
    numbers = [[int(num) for num in list] for list in numbers]
    '''
    To get to any element in the triangle there is:
      - exactly one path -- if it is edge element  [[ leftmost or rightmost]
      - exactly two paths - if not an edge element. 
      We're interested in the path that is higher of the two. 
    '''
    sum_num = {0:{0:numbers[0][0]}}             # initialize the triangle walk : topmost number
    for i in range(1, len(numbers)):            # walk thru each row
        sum_num[i] = {}
        for j in range(0, i+1):
            previous = [0, 0]
            # If this is this the first element of the row, ignore
            if(j-1 >= 0): previous[0] = sum_num[i-1][j-1]
            # If this is this the last element of the row, ignore
            if(j != len(numbers[i]) - 1): previous[1] = sum_num[i-1][j]
            sum_num[i][j] = numbers[i][j] + max(previous)
    print("max_path = ", max(sum_num[len(numbers) - 1].values()))


import time      # get a sense of the time taken
t = time.time()  # get time just before the main routine

########## the main routine #############

if __name__ == "__main__":
    max_path_sum()

########## end of main routine ###########

t = time.time() - t  # and now, after the routine
print("time       = {:7.5f} s\t{:7.5f} ms\t{:7.3f} µs".format(t, t * 1000, t * 100000))