n=int(input("How many Rows are there?\n"))
for a in range(n,0,-1):
    for b in range(n,a-1,-1):
        print(b,end=' ')
    print()