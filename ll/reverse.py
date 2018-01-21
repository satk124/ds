import sys
import pdb

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Llist:
    def __init__(self):
        self.head_ref = None

    # @classmethod
    def rev(self, cur):

        head = cur
        if not (head and head.next):
            "terminated"
            return head;
        else:
            this = head
            head = self.rev(head.next)

            this.next.next = this
            # print "called", head.data, this.data
            return head


    # @classmethod
    def build_ll(self, ar):
        if not ar:
            print "Empty Array"
        self.head_ref = Node(ar[0])
        cur = self.head_ref
        for el in ar[1:]:
            cur.next = Node(el)
            cur = cur.next

    # @classmethod
    def print_ll(self):

        head = self.head_ref
        while(head):
            print "{}->".format(head.data),
            head = head.next
        print ""

def ll_test():
    # pdb.set_trace()
    ll = Llist()
    ll_data = [1,2,3,4,5]
    ll.build_ll(ll_data)
    ll.print_ll()

    # reverse wrapper
    head = ll.head_ref
    ll.head_ref = ll.rev(ll.head_ref)
    head.next = None
    ll.print_ll()

def main(args):
    ll_test()


if __name__ == '__main__':
    main(sys.argv)