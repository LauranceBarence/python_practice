class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# def add_two_numbers(l1, l2):
#     str_l1 = parse_number(l1)
#     str_l2 = parse_number(l2)
#     str_l3 = str(int(str_l1) + int(str_l2))
#     str_l3 = ''.join([x for x in str_l3[::-1]])
#     l3 = parse_node(str_l3)
#     print(parse_number(l3))
#
#
def parse_number(listnode):
    if not listnode.next:
        return str(listnode.val)
    else:
        return parse_number(listnode.next) + str(listnode.val)


#
#
# def parse_node(val, previews_node=None):
#     if previews_node:
#         if len(val) == 1:
#             return ListNode(int(val))
#         elif len(val) > 1:
#             previews_node.next = ListNode(val[0])
#             previews_node.next.next = parse_node(val[1:], previews_node.next)
#             return previews_node.next
#     else:
#         node = ListNode(int(val[0]))
#         node.next = parse_node(val[1:], node)
#         return node

# def add_two_numbers(l1, l2):
#     return add_two_numbers(l1, l2, None)


def add_two_numbers(l1, l2, prev):
    val1 = 0
    val2 = 0
    next1 = None
    next2 = None
    if l1:
        val1 = l1.val
        next1 = l1.next
    if l2:
        val2 = l2.val
        next2 = l2.next
    new_node = ListNode(val1 + val2)
    if prev:
        if prev.val >= 10:
            prev.val %= 10
            new_node.val += 1
    if next1 or next2:
        new_node.next = add_two_numbers(next1, next2, new_node)
    elif new_node.val >= 10:
        new_node.next = add_two_numbers(next1, next2, new_node)
    return new_node


l1 = ListNode(1)
l1.next = ListNode(8)
l2 = ListNode(0)
l3 = add_two_numbers(l1, l2, None)
print(parse_number(l3))
