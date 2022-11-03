# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None:
            return ""
        
        res = ""
        
        def pre(root, res):
            if root.left == None and root.right != None:
                res += str(root.val)
                res +=  "()"
                res += "("
                res = pre(root.right, res)
                res += ")"
                return res
            
            elif root.left == None and root.right == None:
                res += str(root.val)
                return res
            
            elif root.left != None and root.right == None:
                res += str(root.val)
                res += "("
                res = pre(root.left, res)
                res += ")"
                return res
            
            else:
                res += str(root.val)
                res += "("
                res = pre(root.left, res)
                res += ")"
                res += "("
                res = pre(root.right, res)
                res += ")"
                return res
        
        return pre(root, res)
                
        