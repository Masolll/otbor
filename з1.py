from fnmatch import*
k=0
for i in range(0,10**9,777):
    if fnmatch(str(i), "*1?23"):
        k+=1
print(k)
    
