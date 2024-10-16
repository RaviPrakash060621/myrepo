i=int(input('enter numbers of rows in matrix'))
j=int(input('enter numbers of column in matrix'))
a=[]

for x in range(1,j+1):
         for y in range (1,i+1):
                print("enter element of ",x,"row",y,"column")
                x=int(input())
                a.append(x)

r=0
print ('matrix ix :')
for p in range(1,i+1):
    for q in range(1,j+1):
        print(a[r],end=' ')
        r=r+1
    print( )