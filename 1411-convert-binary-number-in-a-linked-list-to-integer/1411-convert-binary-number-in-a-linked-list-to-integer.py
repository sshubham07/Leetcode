# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s=""
        while head:
            s+=str(head.val)
            head=head.next
        s = s[::-1]
        ans = 0
        p=0
        for i in s:
            if i=='1':
                ans+=pow(2,p)
            p+=1
        return ans
        