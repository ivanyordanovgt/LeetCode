from utils.linked_list import linked_list_to_list, create_linked_list, ListNode
from collections import deque

def removeNthFromEnd(head, n):
    n -= 1
    stack = [head]

    while stack[-1].next:
        stack.append(stack[-1].next)

    n = len(stack)-n-1
    stack[n] = None
    dummy = ListNode(0)
    current = dummy

    for el in stack:
        if el is not None:
            print(el)
            current.next = ListNode(el.val)
            current = current.next

    return dummy.next


input = create_linked_list([1,2])
result = removeNthFromEnd(input, 1)
print(linked_list_to_list(result))
