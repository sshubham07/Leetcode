# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        ans = head
        temp = head
        prev = None
        while temp:
            if temp.val in nums and temp==head:
                temp = temp.next
                head = temp
            elif temp.val in nums:
                prev.next = temp.next
                temp=prev.next
            else:
                prev=temp
                temp = temp.next
        return head

        