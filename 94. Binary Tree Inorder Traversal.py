# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    '''def name(self,i,t,lst,root_node):    # no need
        if root_node.val == None or root_node.val == 'null' :
            return None
        
        try: 
            a = lst[i+t]
            root_node.left = TreeNode(val = a)
        except:
            root_node.left = TreeNode(val = None)# might need to change to null
        try :
            a = lst[i+t+1]
            root_node.right = TreeNode(val = a)
        except:
            root_node.left = TreeNode(val = None)# might need to change to null
        
        self.name(i+t, t+1,lst,root_node.left)
        self.name(i+t+1,t+2,lst,root_node.right)
    '''
    def inorderTraversal(self, root):
        if len(root) == 0:
            return []
        #root_node = TreeNode(val = root[0]) 
        #self.name(0,1,root,root_node)
        ans = []
        stk = []
        curr = root

        while curr is not None or len(stk) > 0:
            while curr is not None:       
                stk.append(curr)
                curr = curr.left
            
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans
