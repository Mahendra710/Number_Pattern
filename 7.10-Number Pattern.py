def num(n1):
    if n1==1:
        return 1
    else:
        return n1+num(n1-1)

n=int(input("Enter the number of rows:"))
k=num(n)
for row in range(n):
    val=k-row
    dec=n-1
    for col in range(row+1):
        print(format(val,"<3"),end=" ")
        val=val-dec
        dec=dec-1
    print()