class Solution(object):
    def preorderTraversal(self, root):
        ans = []
        stk = []
        curr = root

        while curr is not None or len(stk) > 0:
            
            while curr is not None:       
                ans.append(curr.val)
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            curr = curr.right
            
        return ans
