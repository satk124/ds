#!/usr/bin/python
'''
Kadane’s Algorithm:
src: http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''

import sys

def largest_sum_contigious(ar=None):
    max_ending_here, max_so_far = 0,0
    for e in ar:
        max_ending_here = max_ending_here + e
        if max_ending_here< 0:
            max_ending_here = 0
        if max_ending_here> max_so_far:
            max_so_far = max_ending_here
    return  max_so_far


def main(args):
    ar = [-2, -3, 4, -1, -2, 1, 5, -3]
    print largest_sum_contigious(ar)
    ar = [-2, -3, -4, -1, -2, 1, 5, -3]
    print largest_sum_contigious(ar)
    ar = [-2, 10, -4, -1, -2, 1, 5, -3]
    print largest_sum_contigious(ar)


if __name__ == '__main__':
    main(sys.argv)
