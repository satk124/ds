#!/usr/bin/python

import sys
# from my_math import gcd
'''
src: 
https://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm
'''


def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)


def juggling(d, ar=None):
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


def main(args):
    ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    d = 3
    juggling( d, ar)


    print "array...",ar
if __name__ == '__main__':
    main(sys.argv)
