a=[1,1,1,1,1,1,1,1,1]
b=[2,2,2,2,2,2,2,2,2]
c=[]
i=3
j=3



for k in range (i*j):
    z=int(a[k])+int(b[k])
    print(z) 
    c.append(z)
z=None
print(c)



# r=0
# for k in range (1,i*j+1):
#     z=int(a[r])+int(b[r])
#     print(z)
#     r=r+1
#     c.append(z)
# z=None
# print(c)



r=0
for p in range(1,i+1):
    for q in range(1,j+1):
        print(c[r],end=' ')
        r=r+1
    print( )
   
'clear'