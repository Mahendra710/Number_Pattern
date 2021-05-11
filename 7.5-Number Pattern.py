n=int(input("How many Rows are there?\n"))
num=1
for a in range(1,n+1):
    for b in range(1,a+1):
        print(num,end=" ")
        num=num+1

    print()