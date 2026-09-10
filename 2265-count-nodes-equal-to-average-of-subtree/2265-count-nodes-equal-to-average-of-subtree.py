# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calc(self,root):
        if not root:
            return (0,0)
        left_sum,count_left = self.calc(root.left)
        right_sum,count_right = self.calc(root.right)
        if (left_sum+right_sum+root.val)//(count_left+count_right+1)==root.val:
            self.count+=1
        return (left_sum+right_sum+root.val,count_left+count_right+1)
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.count = 0
        self.calc(root)
        return self.count
        