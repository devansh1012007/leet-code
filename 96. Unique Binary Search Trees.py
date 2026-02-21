# formula for finding all the binary unique trees that can be formed from "n" nodes is --> (2n)!/((n+1)!*n!) <-- Catalan Number
import math
def numTrees(self, n):
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n+1))

def numTrees2(self, n):
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for node in range(2, n+1):
        for root in range(1,node+1):
            dp[node] += dp[root-1] * dp[node - root]# at any node u can find all the possible combination by multiplying subtrees on left times subtree on right
    return dp[n]
    