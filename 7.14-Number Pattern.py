num=int(input("Enter the number of rows:"))
for i in range(num):
    k=111
    for j in range(num-i-1):
        print(format(" ","<4"),end=" ")
    for j in range(i+1):
        print(format(k,"<4"),end=" ")
        k=k+111
    print()