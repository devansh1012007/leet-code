
def strStr(haystack, pin):
    i3 = 0
    while i3 < len(haystack) :
        i2 = i3
        idx = 0
        for i in haystack:
            if i == pin[idx]:
                i3 = i3 + 1
            #print(haystack[i])
            #print(i , i2)
            
                if i3 - i2 != len(pin)-1 :
                    i = i + 1
                    
                    print(len(pin))
                else : 
                    return i2
            idx = idx + 1
            # i is not increaseing 
#                print ("it passed if ")
                
#                print ("it passed if ")
    print("else")
    print("passed while main")
    return -1
haystack = "monkeymymonkey" 
pin = "my"
print(strStr(haystack, pin))



# sol 1

