# try 1 , 0ms; beats 100% ;
class Solution(object):
    def __init__(self):
        self.deepest_ = 0
    def maxDepth(self, root,deepest=0):
        if not root:
            return 0
        deepest += 1
        if deepest >= self.deepest_: self.deepest_ = deepest
        self.maxDepth(root=root.left,deepest=deepest)
        self.maxDepth(root=root.right,deepest=deepest)
        return self.deepest_

#### BETTER VERSION ; AFTER LEARNING ABT QUES ; STILL NEED PRACTICE THO

class Solution(object):
    def maxDepth(self, root):
        ans = 0
        que = []
        que.append(root)
        while que:
            ans += 1
            for _ in range(len(que)):# exploring all the nodes at 1 level ; v can add append to ans to get back values too 
                node = que.pop(0)
                if node.left :
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
                
        return ans