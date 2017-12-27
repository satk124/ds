#!/usr/bin/python
'''
Kadane’s Algorithm:
src: http://www.geeksforgeeks.org/largest-sum-contiguous-subarray/
'''

import sys
from my_math import gcd


def segment_sum_query():
    #TODO sum/min/gcd
    pass

def square_root_decomposition(ar):
    #TODO sum/min
    pass

def juggling(d, ar=None):
    '''
    src: 
    https://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm
    '''
    l = len(ar)
    g = gcd(d,l)
    for i in xrange(g):
        prev = i
        t = ar[i]
        walk = (i+d)%l
        while walk !=i :
            ar[prev] = ar[walk]
            prev = walk
            walk = (walk+d)%l
        ar[(walk-d)%l] = t


def largest_product_subarray(ar):
    pass


def largest_sum_subarray(ar=None):
    max_ending_here, max_so_far = 0,0
    for e in ar:
        max_ending_here = max_ending_here + e
        if max_ending_here< 0:
            max_ending_here = 0
        if max_ending_here> max_so_far:
            max_so_far = max_ending_here
    return  max_so_far


def longest_bitonic_subsequence(ar):
    # TODO longest bitonic subsequence
    pass


def bitonic_subarray_length(ar):
    '''
    reverse bitonic
    '''
    max_len, curlength = 1, 1
    d_flag, i_flag = True, False
    pre_el = ar[0]
    for e in ar[1:]:
        #print e, d_flag, i_flag, max_len, curlength, pre_el
        if not i_flag and not d_flag:
            d_flag = True
            pre_el = e
            curlength = 1
        if not i_flag and d_flag:
            if e>=pre_el:
                i_flag = True

                d_flag = False

            else :
                curlength+=1

        if i_flag and e>=pre_el:
            curlength += 1
        elif i_flag:
            i_flag = False
        if curlength > max_len:
            max_len = curlength
        pre_el = e
    return max_len


def three_way_partition(ar, lowVal, highVal):
    lowI, highI = 0, len(ar)-1
    for i, e in enumerate(ar):
        i = 0
    while(i<highI):
        #print ar, i
        if ar[i] <lowVal:
            ar[i], ar[lowI] = ar[lowI], ar[i]
            lowI += 1
            i += 1
        elif ar[i]> highVal:
            ar[i], ar[highI] = ar[highI], ar[i]
            highI -= 1
        else:
            i+=1


def kth_largest_no(ar, k):
    #TODO 1. heap method 2. quick sort 3. randomized quick sort
    pass


def largest_subarray_with_equal01():
    '''
    :return: 
    '''
    pass


def kth_smallest_in_sorted_matrix(mat):
    # 10, 20, 30, 40
    # 15, 25, 35, 45
    # 24, 29, 37, 48
    # 32, 33, 39, 50
    # The 3rd smallest element is 20 and 7th smallest element is 30
    pass


def main(args):
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    juggling(3, ar)
    print "rotated array...", ar
    #---------------------------------
    ar = [-2, -3, 4, -1, -2, 1, 5, -3]
    print largest_sum_subarray(ar)
    ar = [-2, -3, -4, -1, -2, 1, 5, -3]
    print largest_sum_subarray(ar)
    ar = [-2, 10, -4, -1, -2, 1, 5, -3]
    print largest_sum_subarray(ar)
    #------------------------------------
    ar = [1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32]
    three_way_partition(ar, 14, 20)
    #-----------------------------------
    print "bitonic length: ", bitonic_subarray_length([12, 4, 78, 90, 45, 23])
    print "bitonic length: ", bitonic_subarray_length([20, 4, 1, 2, 3, 4, 2, 10])
    print "bitonic length: ", bitonic_subarray_length([12, 4, 78, 90, 45, 23])


if __name__ == '__main__':
    main(sys.argv)
