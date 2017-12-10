#!/usr/bin/python

import sys

'''
src: 
https://stackoverflow.com/questions/23321216/rotating-an-array-using-juggling-algorithm
'''


def juggling(d, ar=None):
    l = len(ar)
    for i in xrange(d):

        t = ar[i]

        while(i+d<l):
            ar[i]= ar[i+d]
            i = i+d

        ar[i] = t

def main(args):
    ar = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    juggling( d, ar)


    print "array...",ar
if __name__ == '__main__':
    main(sys.argv)
