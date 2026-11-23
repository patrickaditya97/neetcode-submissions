# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        deque = collections.deque()

        dummy = head
        while dummy:
            deque.append(dummy)
            dummy = dummy.next

        dummy = deque.popleft()
        while deque:
            dummy.next = deque.pop()
            dummy = dummy.next
            
            if deque:
                dummy.next = deque.popleft()
                dummy = dummy.next

        dummy.next = None

