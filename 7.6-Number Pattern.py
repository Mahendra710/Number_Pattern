n=int(input("How many rows are there?\n"))
for a in range(n,0,-1):
    for b in range(1,a+1):
        print(b,end=" ")
    print()