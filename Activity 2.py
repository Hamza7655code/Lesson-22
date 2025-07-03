def palind(t):
    e = len(t) -1
    s = 0
    while s>e:
        if t[s]!=t[e]:
            return False
        else:
            s+=1
            e-=1
    return True
t1 = (1,2,3,3,2,1)
if(palind(t1)):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
            
        
    