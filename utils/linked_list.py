# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(lst):
    if not lst:  # If the list is empty, return None
        return None

    # Initialize the head of the linked list
    head = ListNode(lst[0])
    current_node = head

    # Iterate over the remaining elements in the list
    for value in lst[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next

    return head


def linked_list_to_list(head):
    result = []
    current_node = head

    # Traverse the linked list and collect values
    while current_node:
        result.append(current_node.val)
        current_node = current_node.next

    return result