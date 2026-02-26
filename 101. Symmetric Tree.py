# BETTER APPROCH --> 2nd try
class Solution(object):
    def ChildrenVar(self,left,right):
        if left is None and right is None:
            return True
        elif left and right:
            if left.val != right.val:
                return False
        else: return False
        return (self.ChildrenVar(left.left, right.right) and self.ChildrenVar(left.right, right.left))
         
    def isSymmetric(self, root):
        return self.ChildrenVar(root.left, root.right)
    
###############
# 1st try
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def ChildrenVar(self,left,right):
        if left is None and right is None :
            return True
        elif (left and not right) or (not left and right):
            return False
        elif (left.right and not right.left) or (not left.right and right.left) or (left.left and not right.right) or (not left.left and right.right):
            return False
        elif left.left is None and left.right is None and right.left is None and right.right is None:
            return True
        elif left.right.val != right.left.val or left.left.val != right.right.val:## need to cgange
            return False
        self.ChildrenVar(left.left, right.left)
        self.ChildrenVar(left.right, right.right)
        return True
    def isSymmetric(self, root):
        if (root.left and not root.right) or (not root.left and root.right):
            return False
        elif not root.left and not root.right:
            return True
        elif root.left.val != root.right.val:
            return False
        
        return self.ChildrenVar(root.left, root.right)

#it is not a recursion proble , v need list or quese or stack
# 1st v check if root.left = root.right ?
# then lst or something to store the left ,right root of root.left and left, right root of root.right and then v compair
# then v go down to left left node and check it's children maybe v can make a recursion function, for left and right side of mirror and compare there children and pass on recursion val again . compre this down the tree

### BEST SOLUTION 
# 3rd try
class Solution(object):
    def ChildrenVar(self,left,right):
        if not left and not right :
            return True
        elif not left or not right:
            return False
        return (left.val == right.val and self.ChildrenVar(left.left, right.right) and self.ChildrenVar(left.right, right.left))
         
    def isSymmetric(self, root):
        return self.ChildrenVar(root.left, root.right)  
    
###### Bestest solution 
# 4th try 
class Solution(object):
    def ChildrenVar(self,left,right):
        if not left and not right :
            return True
        elif not left or not right:
            return False
        return left.val == right.val and self.ChildrenVar(left.left, right.right) and self.ChildrenVar(left.right, right.left)
         
    def isSymmetric(self, root):
        return self.ChildrenVar(root.left, root.right)