# Project Euler
Solutions of the problems from https://projecteuler.net/ written in Python 3.

The original challenge is to find solution for each of these problems, that execute in less than a minute. But, my personal goal has been to optimize the code to finish it under a second!
Primarily to take away the advances in the computing power as the primary reason for the speedy code. 

Of course in quite a few cases, I have first resorted to the brute-force method to get the logic right. Once past that tried to explore the reason for slowness, and perform optimization. Some of the solutions discussed in the forum are indeed exceptionally clever, and I've learnt a lot going over them.
#### Organization
Each problem is saved as a separate file, and each of them can be invoked independent of each other. That said, a collection of the utility functions used by more than one problem is stored in the `common.py` file, which would be required for some of the problems. 

Given the large number of problems, for easier readability, they are grouped in sets of 25, and stored in separate folders. The use of additional modules is minimal, and restricted only to those included in the default installation.

```buildoutcfg
common.py                utilities invoked in the solutioning of more than one problem.
p0001_0050/
     p0001.py
     p0002.py
     ...
     p0050.py
p0051_0100/
     p0051.py
     p0052.py
     ...
     p0100.py
...
```

## How to Use
If downloading the entire collection:
```buildoutcfg
cd <problem-folder>
python3 <problem-file>.py
```