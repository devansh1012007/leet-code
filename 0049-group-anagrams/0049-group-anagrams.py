from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_={}
        for i in strs:
            j = ''.join(sorted(i))
            if j in hash_: hash_[j].append(i)  
            else: hash_[j] = [i]
        ans=[]
        for value in hash_.values():
            ans.append(value)
        return ans