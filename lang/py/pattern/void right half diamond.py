a = int(input("enter height of half diamond"))

for i in range(1,a):
    for j in range(a):
        if j<i-1:
            print(" ",end=" ")
        else:
            print("*",end=' ')
    print( )

for i in range(a,0,-1):
    for j in range(a):
        if j>=i-1:
            print("*",end=' ')
        else :
            print(" ",end =' ')
    print( )