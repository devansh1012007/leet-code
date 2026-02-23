# 100. Same Tree
# EASY

# Solution 1
    
class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None: 
            return True
        if p is None or q is None:
            return False
        if p.val != q.val :
            return False
        if self.isSameTree(p.left,q.left) is False:
            return False
        if self.isSameTree(p.right, q.right) is False:
            return False
        return True
        
# Solution 2

class Solution(object):
    def isSameTree(self, p, q):
        a = []
        p_ = []
        q_ = []
        while p is not None or len(a)>0:
            if p is None:
                p_.append(0)
            while p is not None:
                a.append(p)
                p = p.left
            p = a.pop()
            d=p.val
            if d is None:
                d=0
            p_.append(d)
            p = p.right
        a = []
        while q is not None or len(a)>0:
            if q is None:
                q_.append(0)
            while q is not None:
                a.append(q)
                q = q.left
            q = a.pop()
            d= q.val
            if d is None:
                d = 0
            q_.append(d)
            q = q.right
        
        return p_ == q_
