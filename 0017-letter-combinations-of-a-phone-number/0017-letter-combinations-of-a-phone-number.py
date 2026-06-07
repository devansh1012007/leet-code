class Solution(object):
    def letterCombinations(self, digits):
        table = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],}
        sol=[]
        for i in digits:
            table_i = table[i]
            len_sol = len(sol)
            if len_sol ==0:
                for j in table_i:sol.append(j)
            while len_sol>0:
                prev_letter = sol[0]
                for j in table_i:sol.append(prev_letter+j)
                sol.pop(0)
                len_sol-=1
        return sol

        '''for i in w_list[-1]:sol.append(i)
        n=2

        while n <= len(w_list):
            for i in sol:
                for j in w_list[-n]:
                    sol2.append(j+i)
            sol = sol2
            n+=1
        return sol
'''
# core logic 1 
"""    function():
        w_list=[]
        table = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],}
        for i in digits:w_list.append(table[i])
        # need some refine ment here; v can save memory

        '''
        logic : we will go backwards
        1st v will add all the items from last list to sol
        then we will recusivly rewrite sol as we ittrate through the list in reverse 
        apparently leetcode is not taking reverse order

        for i in w_list[-1]:sol.append(i)
        n=2
        while n <= len(w_list):
            for i in sol:
                for j in w_list[-n]:
                    sol2.append(i+j)
            sol = sol2
            n++
        return sol
        '''
        for i in w_list[-1]:sol.append(i)
        n=2
        while n <= len(w_list):
            for i in sol:
                for j in w_list[-n]:
                    sol2.append(i+j)
            sol = sol2
            n+=1
        return sol
"""