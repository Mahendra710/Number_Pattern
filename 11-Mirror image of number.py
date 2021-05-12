n=int(input("How many rows are there?\n"))
for a in range(1,n+1):
    for b in range(1,a+1):
        print(b,end=" ")
    for s in range(2*a,2*n): #2(n-a)
        print(" ",end=" ")
    for c in range(a,0,-1):
        print(c,end=" ")
    print()