# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        n=0
        temp = head
        while temp:
            temp=temp.next
            n+=1
        n//=2
        temp=head
        prev=head
        count=0
        while count<n:
            prev=temp
            temp=temp.next
            count+=1
        prev.next=temp.next
        return head

        