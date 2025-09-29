# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        dummy = ListNode(0)
        tail = dummy
        while l1 is not None and l2 is not None or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            
            digit = s % 10
            carry = s // 10
            tail.next = ListNode(digit)
            tail = tail.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

# --- Helpers for testing ---
def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# --- Test cases ---
if __name__ == "__main__":
    sol = Solution()

    # Example 1
    l1 = build_linked_list([2,4,3])
    l2 = build_linked_list([5,6,4])
    result = sol.addTwoNumbers(l1, l2)
    print("Example 1:", linked_list_to_list(result))  # [7,0,8]

    # Example 2
    l1 = build_linked_list([0])
    l2 = build_linked_list([0])
    result = sol.addTwoNumbers(l1, l2)
    print("Example 2:", linked_list_to_list(result))  # [0]

    # Example 3
    l1 = build_linked_list([9,9,9,9,9,9,9])
    l2 = build_linked_list([9,9,9,9])
    result = sol.addTwoNumbers(l1, l2)
    print("Example 3:", linked_list_to_list(result))  # [8,9,9,9,0,0,0,1]