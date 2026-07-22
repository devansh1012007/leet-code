class Solution_2:
    # simple sol without DP coz i was having hard to visualizes how to exicute
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        # now we need a matrix or arr type situation where we save the value or sum of shit so that we don't need to re calculate shit
        # we can to top to bottom and bottom to top 
        # i am facing exicution issues --> not sure how to write code
        if numRows == 1 :return [[1]]
        if numRows == 2: return [[1],[1,1]]
        ans=[[1],[1,1]]
        numRows -= 2
        while numRows > 0:
            temp = [1]
            prev = ans[-1]
            i=0
            lenght = len(prev)
            while i+1 < lenght:
                temp.append(prev[i]+prev[i+1])
                i+=1
            temp.append(1)
            ans.append(temp)
            numRows -=1
        return ans
    '''
    # attempt to include DP:
    '''
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 :return [[1]]
        if numRows == 2: return [[1],[1,1]]
        ans=[[1],[1,1]]
        # idk how to fit it in arr ; also i need to make it into a recursive func next
        numRows -= 2
        while numRows > 0:
            temp = [1]
            prev = ans[-1]
            i=0
            lenght = len(prev)
            #print("lenght : ", lenght)
            if lenght%2 ==0:
                print("even")
                while i+1 <= lenght/2:
                    print("i+1 : ",i+1)
                    temp.append(prev[i]+prev[i+1])
                    i+=1
                    print("temp : ",temp)
                #print("i : ", i )
                temp2 = temp
                print("temp : ",temp)
                temp2.pop()
                print("temp2 : ",temp2[::-1])
                for j in temp2[::-1]: temp.append(j)
                #temp = [*temp, *temp2] ### why is it not working ????
                print("temp final :", temp)
            else: 
                print("odd")
                while i+1 <= lenght//2:
                    temp.append(prev[i]+prev[i+1])
                    i+=1
                #print("i : ", i )
                temp = temp + temp[::-1]
            
            ans.append(temp)
            numRows -=1
        return ans
        # need to make it recursive and also make it use a dedicated system 

    '''    
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 :return [[1]]
        if numRows == 2: return [[1],[1,1]]
        ans=[[1],[1,1]]
        numRows -= 2
        return self.recursion(numRows,ans)
    def recursion(self, numRows: int, ans : List[[List[int]]]) -> List[List[int]]:
        print("--------------- " ,numRows )
        if numRows > 0:
            prev = ans[-1]
            i=0
            length = len(prev)
            temp = [1]*(length+1)
            if length%2 ==0:
                #print("even")
                while i+1 <= length/2:
                    #print("i+1 : ",i+1)
                    temp[i+1] = (prev[i]+prev[i+1])
                    i+=1
                    #print("temp : ",temp)
                print("i [even] : ", i )
                temp2 = temp[:i]
                print("temp [even] : ",temp)
                #temp2.pop()
                print("temp2 [even] : ",temp2[::-1])
                for j in temp2[::-1]: 
                    temp[i+1] = j
                    i+=1
                #temp = [*temp, *temp2] ### why is it not working ????
                #print("temp final :", temp)
            else: 
                #print("odd")
                while i+1 <= length//2:
                    temp[i+1] = (prev[i]+prev[i+1])
                    i+=1
                print("i [odd]  : ", i )
                temp2 =temp[:i+1]
                print("temp [odd] : ", temp) 
                print("temp2 [odd] : ", temp2) 
                for j in temp2[::-1]: 
                    temp[i+1] = j
                    i+=1
            ans.append(temp)
            numRows -=1
            return self.recursion(numRows, ans)
        else : return ans

# clean answer:
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1 :return [[1]]
        if numRows == 2: return [[1],[1,1]]
        ans=[[1],[1,1]]
        numRows -= 2
        return self.recursion(numRows,ans)
    
    def recursion(self, numRows: int, ans : List[[List[int]]]) -> List[List[int]]:
        
        if numRows > 0:
            prev,i = ans[-1],0
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
            ans.append(temp)
            numRows -=1
            return self.recursion(numRows, ans)
        else : return ans