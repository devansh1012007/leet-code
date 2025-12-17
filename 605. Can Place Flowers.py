class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        i = 0 
        while i < len(flowerbed)and n>0:
            if flowerbed[i] == 1:
                i+=2
            else:
                try:
                    if flowerbed[i+1]==0:##basicly v r tryint to put pointer at index where value of previous index is 0 
                        n -=1
                        i += 2
                    else:
                        i +=1  
                except:
                    if flowerbed[i-1]==0:# for [1,0,0]; code will jumt to i=2 and then v check of this condition
                        n-=1
                        i +=2 
        return True if n == 0 else False # so cool 1 liner right ?

# test case 
#[0,0,1,0,0,1,0,1,0,1,0,0,1,0,0,0,0,0,1,0,0]
# n = 4 ; true

## Another way to do it
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    
        for i in range(len(flowerbed)):
            left = i == 0 or flowerbed[i-1] == 0
            right = i == len(flowerbed) - 1 or flowerbed[i+1] == 0

            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0