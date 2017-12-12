#!/usr/bin/python


import sys
from util import debug

#@debug
def heapify(ar, i, l):
    left = 2*i+1
    right = 2*i+2
    large = i
    if left< l and ar[left] >ar[i]:
        large = left
    if right <l and ar[right] > ar[large]:
        large = right
    if i != large:
        ar[i], ar[large] = ar[large], ar[i]
        heapify(ar, large, l)


def build_heap(ar):
    l = len(ar)
    for i in xrange(l/2-1 , -1, -1):
        heapify(ar, i, l)


def heap_sort(ar):
    l = len(ar)
    for i in xrange(l-1,0,-1):
        ar[i] , ar[0]= ar[0] , ar[i]
        heapify(ar, 0, i)


def main(args):
    ar = [1, 23, 12, 9, 30, 2, 50]
    build_heap(ar)
    heap_sort(ar)

    print ar


if __name__ == '__main__':
    main(sys.argv)
