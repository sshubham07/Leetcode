# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        st=[]
        temp = head
        while temp:
            st.append(temp)
            temp=temp.next
        n=len(st)
        ans = 0
        temp=head
        for i in range(n//2):
            ans=max(ans,temp.val+st[-1].val)
            st.pop()
            temp=temp.next
        return ans
        