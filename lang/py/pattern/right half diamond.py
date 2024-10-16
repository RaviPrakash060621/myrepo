a = int(input("enter height of half diamond"))

for i in range(1,a+1):
    for j in range(i):
        print("*",end =' ')
    print( )

for i in range(a-1,0,-1):
    for j in range(i):
        print("*",end =' ')
    print( )