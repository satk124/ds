import sys

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


def swap_node(head, key1, key2):
    curr = head
    prev = head
    curr = curr.next
    p1, p2 = None, None
    if key1 == key2:
        print "nice kidding.."
        return

    while curr:
        print "im running.."
        if curr.data == key1:
            # print "got", key1, prev.data
            p1 = prev
        if curr.data == key2:
            # print "got", key2, prev.data
            p2 = prev
        if p1 and p2:
            break
        prev = curr
        curr = curr.next

    k1 = p1.next
    k2 = p2.next
    save_p2 = None
    # swap next pointer
    if p2 == k1:
        save_p2 = p1.next

    temp = k1.next
    k1.next = k2.next
    k2.next = temp



    # swap the position of nodes
    temp = p1.next
    # print "temp", temp.data
    # print "p1", p1.data
    # print "p2", p2.data
    if save_p2:
        p1.next = save_p2.next
    else:
        p1.next = p2.next

    p2.next = temp


    # p1.next = p2.next
    # t2 = p2.next.next
    #
    # p2.next = temp.next
    # temp.next = t2
    #

    # temp1 = p2.next


def print_ll(head):
    while head != None:
        print head.data
        head = head.next


def main(args):
    nodes = [1, 2, 3, 4, 5, 6]
    head = Node(None, None)
    ll, curr = None, head
    # if nodes:
    #     ll = Node(nodes[0], None)
    #     curr = ll
    # if not curr:
    #     print "you failed:)"
    #     return
    for n in nodes:
        node = Node(n, None)

        curr.next = node
        curr = curr.next
    print_ll(head.next)
    key1, key2 = 3, 4

    # raw_input("key to swap").split()[:2]

    swap_node(head, key1, key2)
    print_ll(head.next)


if __name__ == '__main__':
    main(sys.argv)