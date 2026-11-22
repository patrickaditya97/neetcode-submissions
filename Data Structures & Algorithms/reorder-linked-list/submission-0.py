# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        slow.next = None

        head1, head2 = head, prev
        while head2:
            temp1, temp2 = head1.next, head2.next
            head1.next, head2.next = head2, temp1
            head1, head2 = temp1, temp2