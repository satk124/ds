#!/usr/bin/python


import sys

def swap(A, i, j):
    A[i] , A[j] = A[j], A[i]


def reverse_array(A):
    j = len(A)-1
    i = 0
    while i < j:
        swap(A, i, j)
        i+=1
        j-=1

def main(args):
    A = [1, 2, 3, 4, 5, 6]
    reverse_array(A)
    print A


if __name__ == '__main__':
    main(sys.argv)
