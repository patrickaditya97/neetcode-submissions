# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result_node = ListNode(0)
        dummy = result_node

        while list1 and list2:
            
            if list1.val < list2.val:
                temp = list1.next
                dummy.next = list1
                dummy = dummy.next
                list1 = temp
            elif list1.val > list2.val:
                temp = list2.next
                dummy.next = list2
                dummy = dummy.next
                list2 = temp
            else:
                first, second = list1.next, list2.next

                dummy.next = list1
                dummy = dummy.next
                dummy.next = list2
                dummy = dummy.next

                list1, list2 = first, second

        while list1:
            dummy.next = list1
            dummy = dummy.next
            list1 = list1.next
        
        while list2:
            dummy.next = list2
            dummy = dummy.next
            list2 = list2.next

        return result_node.next
                