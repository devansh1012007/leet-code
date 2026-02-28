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