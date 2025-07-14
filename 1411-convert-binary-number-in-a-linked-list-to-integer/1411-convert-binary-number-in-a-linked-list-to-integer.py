# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        curr=head
        l=""
        while curr:
            l+=str(curr.val)
            curr=curr.next
        return int(l,2)
