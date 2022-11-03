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
                res += f"{str(root.val)}()({pre(root.right, res)})"
                return res
            
            elif root.left == None and root.right == None:
                res += str(root.val)
                return res
            
            elif root.left != None and root.right == None:
                res += f"{str(root.val)}({pre(root.left, res)})"
                return res
            
            else:
                res += f"{str(root.val)}({pre(root.left, res)})({pre(root.right, res)})"
                return res
        
        return pre(root, res)
                
        