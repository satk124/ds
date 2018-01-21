#!/usr/bin/python


import sys


def gcd(x, y):
    '''
    Euclidean algorithm:
    explanation: https://stackoverflow.com/questions/6005582/how-does-the-euclidean-algorithm-work/6005795#6005795
    '''
    if y == 0:
        return x
    else:
        return gcd(y, x%y)


def main(args):
    print(gcd(6,8))
    print(gcd(8,6))

if __name__ == '__main__':
    main(sys.argv)
