# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        q = deque([root])
        curLvl = []
        while q:

            for i in range(len(q)):
                curElem = q.popleft()
                curLvl.append(curElem.val)
                if curElem.left:
                    q.append(curElem.left)
                if curElem.right:
                    q.append(curElem.right)
            res.append(curLvl)
            curLvl = []
        
        return res

        