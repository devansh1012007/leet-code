'''
def strStr(haystack, pin):
    i = 0
    while i < len(haystack) :
        i2 = i
        idx = 0
        while haystack[i] == pin[idx]:
            print(haystack[i])
            print(i , i2)
            if i - i2 == len(pin)-1 :
                print(len(pin))
                return i2
            print ("it passed if ")
            i = i + 1
            idx = idx + 1
            print ("it passed if ")
    print("else")
    print("passed while main")
    return -1
haystack = "monkeymymonkey" 
pin = "my"
print(strStr(haystack, pin))
'''
# sol 1 

def strStr(haystack, pin):
    i = 0
    i2 = i
    while i < len(haystack) :
        i2 = i
        idx = 0
        while i < len(haystack) and haystack[i] == pin[idx]:
            #print(haystack[i])
            #print("i =", i, "i2 =", i2, haystack[i])
            #print(i , i2)
            if i - i2 == len(pin) :
                #print(len(pin))
                return i2
            #print ("it passed if ")
            i2 = i
            i = i + 1
            idx = idx + 1
            print("i =", i, "i2 =", i2, haystack[i])
            #print ("it passed if ")
        i = i + 1

    #print("passed while main")
    return -1
haystack = "mississippi"
pin = "issip" # fucked in places like this also i2 in our thougt exp was 1 in right place but in psudo code it was placed at the place where pointer 1 got fucked 