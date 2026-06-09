# logic 1
"""
        # pointer has 2 options --> pointer +- numMoves
        function :
            pointer = numMoves = 0
            while True:
                if pointer + numMoves <= Target and pointer - numMoves >= Target: move --> min(target - (pointer + numMoves),target - (pointer - numMoves));

                elif pointer + numMoves <= Target: move --> pointer += numMoves  

                else: move --> pointer -= numMoves
                if pointer == target : return numMoves 
                numMoves++
"""
# logic 1 wrong assumtion that u can only move +-numMoves; actually v can move from (1 to numMoves) but i am not sure as exmple says other wise.
"""class Solution(object):
    def reachNumber(self, target):
        pointer = 0
        numMoves =0
        while True:
            if pointer + numMoves <= target and pointer - numMoves >= target: 
                if target - (pointer + numMoves) < target - (pointer - numMoves):
                    pointer += numMoves
                else:pointer -= numMoves
            elif pointer + numMoves <= target:
                pointer += numMoves
            else: pointer -= numMoves
            print(pointer)
            if pointer == target : return numMoves 
            numMoves += 1
"""
#logic 1.1 
"""
        # pointer has 2 options --> pointer +- (1 to numMoves)
        function :
            pointer = numMoves = 0
            while True:
                if pointer + numMoves <= target and pointer - numMoves >= target: move --> min(target - (pointer + numMoves),target - (pointer - numMoves));

                elif pointer + numMoves <= target: move --> pointer += numMoves
                elif pointer - numMoves >= target: move --> pointer += numMoves
                else: return numMoves
                if pointer == target : return numMoves 
                numMoves++
"""
# logic 2
"""
class Solution(object):
    def reachNumber(self, target):
        pointer = 0
        numMoves =1
        target =abs(target)
        while True:
            while numMoves <= target - pointer:
                pointer +=numMoves
                print(pointer)
                numMoves += 1
            if target == pointer: return (numMoves - 1)
            else:pointer -=numMoves
            numMoves += 1
"""
# logic 3 
class Solution(object):
    def reachNumber(self, target):
        pointer = 0
        numMoves =0
        target =abs(target)
        while pointer < target:
            numMoves += 1
            pointer +=numMoves

        while(pointer - target)%2 != 0:
            numMoves += 1
            pointer +=numMoves
        return numMoves