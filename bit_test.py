import sys

def get_sum(bit,h):
    h+=1
    sum = 0
    while h>0:
        sum += bit[h]
        h -= h&-h
    return sum

def update_bit(bit, len, i, v):
    i+=1
    while i <= len:
        bit[i] += v
        i += i&-i

def build_bit(ar):
    l = len(ar)
    bit = [0]*(l+1)
    for i in range(l):
        update_bit(bit,l, i, ar[i])
    return bit


def main():
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]

    bit = build_bit(arr)
    assert [0, 2, 3, 1, 7, 2, 5, 4, 21, 6, 13, 8, 30] == bit
    print("bit constructed", bit)
    print("sum 0-5",get_sum(bit,5))
    print("update 5->6", update_bit(bit,len(arr),3, 6))
    print("sum 0-5", get_sum(bit, 5))


if __name__ == "__main__":
    main()
