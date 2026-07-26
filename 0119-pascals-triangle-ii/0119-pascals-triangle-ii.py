class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex +=1
        if rowIndex == 1 :return [1]
        if rowIndex == 2: return [1,1]
        ans=[1,1]
        rowIndex -= 2
        return self.recursion(rowIndex,ans)
    
    def recursion(self, numRows: int, ans : List[[List[int]]]) -> List[List[int]]:
        
        if numRows > 0:
            prev,i = ans,0
            length = len(prev)
            temp = [1]*(length+1)
            if length%2 ==0:
                while i+1 <= length/2:
                    temp[i+1] = (prev[i]+prev[i+1])
                    i+=1
                
                temp2 = temp[:i]
                for j in temp2[::-1]: 
                    temp[i+1] = j
                    i+=1
                
            else: 
                while i+1 <= length//2:
                    temp[i+1] = (prev[i]+prev[i+1])
                    i+=1
                temp2 =temp[:i+1]
                for j in temp2[::-1]: 
                    temp[i+1] = j
                    i+=1
            ans=temp
            numRows -=1
            return self.recursion(numRows, ans)
        else : return ans