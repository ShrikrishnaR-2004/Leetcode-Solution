# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        rev_res=sorted(res,reverse=True)
        print(rev_res)

        curr= None

        for node in rev_res:
            head=ListNode(node)
            head.next=curr
            curr=head
        return head
            
