# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d={}
        count=set()
        for i in descriptions:
            parent = i[0]
            node = i[1]
            left=i[2]
            if node not in d:
                t = TreeNode(node)
                d[node]=t
            count.add(node)
            t = d[node]
            if parent not in d:
                p = TreeNode(parent)
                d[parent]=p
            p=d[parent]
            if left:
                d[parent].left=t
            else:
                d[parent].right=t
        for i in descriptions:
            if i[0] not in count:
                print(d[i[0]].val)
                return d[i[0]]
        return None