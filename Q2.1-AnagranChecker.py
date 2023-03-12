def isAnagram(a, b):
    
    #Unequal Length strings cannot be anagrams
    if len(a) != len(b):
        return False
    
    #sort the first string
    first = sorted(a)
    #sort the second string
    second = sorted(b)
    
    #check if both the strings are the same
    if first == second:
        return True
    else:
        return False
    
#driver code
ans = isAnagram("shore","horse")
print(ans)