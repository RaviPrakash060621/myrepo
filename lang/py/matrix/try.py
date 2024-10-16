print("1st matrix:-")
i=int(input('enter numbers of rows in matrix'))
j=int(input('enter numbers of column in matrix'))
a=[]

for x in range(1,j+1):
         for y in range (1,i+1):
                print("enter element of ",x,"row",y,"column")
                z=int(input())
                a.append(z)
z= None             

r=0
print ('matrix is :')
for p in range(1,i+1):
    for q in range(1,j+1):
        print(a[r],end=' ')
        r=r+1
    print( )

print("2nd matrix:-")    
b=[]

for x in range(1,j+1):
         for y in range (1,i+1):
                print("enter element of ",x,"row",y,"column")
                z=int(input())
                b.append(z)
z= None                

r=0
print ('matrix is :')
for p in range(1,i+1):
    for q in range(1,j+1):
        print(b[r],end=' ')
        r=r+1
    print( )

#addition of matrix
print("addition of matrix is :")
c=[]
for k in range (i*j):
    z=int(a[k])+int(b[k])
    c.append(z)
z=None


r=0
for p in range(1,i+1):
    for q in range(1,j+1):
        print(c[r],end=' ')
        r=r+1
    print( )
   