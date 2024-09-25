n = 5

for i in range(1, n+1):
    
    # adding required spaces before the *
    # we will iterate from i to n
    for j in range(i,n):
        print("_ ", end="")
    
    for k in range(1, 2*i):
        
        if(k==1 or k==2*i-1 or i==n):
            print("*", end=" ")
        elif i==n-1 and k in (2, 2*i-2):
            print(" ", end=" ")
        elif(2<i<n and ((k==2*i-3) or k==3 or i==n-1) ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print("")