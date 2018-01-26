import sys


def print_out(mat):
    print ""
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == 0:
                print " ",
            else: print mat[i][j],
        print ""


def print_patt(n):
    d = 2*n
    mat = [[0]*(d) for i in range(d)]
    x_print = False
    print_out(mat)
    for i in range(1, n+1):
        # print i
        if i%2 == 0: continue
        x, y = i, n
        x_print = not x_print
        for j in range(1, n+1):
            if x>n:
                break
            if x_print:
                mat[x][y] = "X"
            else:
                mat[x][y] = "Y"
            x+=1
            y+=1
    x_print = not x_print
    for i in range(d-1, n-1, -1):

        print i
        if i%2 == 0: continue
        x, y = i, n
        x_print = not x_print
        for j in range(1, n+1):
            if x<n:
                break
            print x, y
            if x_print:
                mat[x][y] = "X"
            else:
                mat[x][y] = "Y"
            x-=1
            y-=1

    # print "out"
    print_out(mat)

    print mat


def main(args):

    '''
    print pattern n=10
                    X
                      X
                    Y   X
                      Y   X
                    X   Y   X
                      X   Y   X
                    Y   X   Y   X
                      Y   X   Y   X
                    X   Y   X   Y   X
  X   Y   X   Y   X   X   Y   X   Y   X
    X   Y   X   Y   X
      X   Y   X   Y
        X   Y   X   Y
          X   Y   X
            X   Y   X
              X   Y
                X   Y
                  X
                    X
    '''
    print_patt(10)
    print 'start code'



if __name__ == '__main__':
    main(sys.argv)