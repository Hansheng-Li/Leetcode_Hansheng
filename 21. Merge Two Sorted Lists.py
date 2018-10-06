# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif l1 and l2 :
            if l1.val <= l2.val:
                temp = l1
                temp.next = self.mergeTwoLists(l1.next, l2)
                return temp
            else:
                temp = l2
                temp.next = self.mergeTwoLists(l1, l2.next)
                return temp
        elif l1:
            temp = l1
            temp.next = self.mergeTwoLists(l1.next, l2)
            return temp
        else:
            temp = l2
            temp.next = self.mergeTwoLists(l1, l2.next)
            return temp
        return None

"""
OR
"""


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy = cur = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 or l2
    return dummy.next