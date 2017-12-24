#!/usr/bin/python

from util import debug
from heap import heapify, build_heap

import sys


def using_max_heap(ar, k):
    l = len(ar)
    build_heap(ar)

    for i in range(k):
        ar[0], ar[l-i-1]  = ar[l-i-1], ar[0]
        heapify(ar, 0, l-i)

    return ar[-k:]


def using_bubble_sort(ar, k):
    ret = []
    l = len(ar)
    for j in xrange(k):

        for i in xrange(l-j-1):
            if ar[i]>ar[i+1]:
                ar[i+1], ar[i] = ar[i], ar[i+1]
        ret.append(ar[l-j-1])
    return ret


def k_largest(ar, k):
     #using_bubble_sort(ar, k)
     return  using_max_heap(ar, k)

def main(args):
    ar = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    print k_largest(ar, k)



if __name__ == '__main__':
    main(sys.argv)
