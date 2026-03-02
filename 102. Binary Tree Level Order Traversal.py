class Solution(object):
    def levelOrder(self, root):
        # dont try to do recursion in this. do it with stack         
        stk = []
        ans = []
        while root or len(stk)>0 :
            while root:
                stk.append(root)
                ans.append([root.val])
                root = root.left
            root = stk[-1]
            if root.right:
                stk.append(root.right)
                ans[len(stk)-1].append(root.right.val)
                root = root.right.left
            else:
                stk.pop()
        return ans

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
            
        return result