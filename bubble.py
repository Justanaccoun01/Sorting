l = [3,4,24,4,3,44,20]

for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if(l[j]>l[j+1]):
            t = l[j+1]
            l[j+1]=l[j]
            l[j]=t
print(l)
            
