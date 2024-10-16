a=[]
r=0
for i in range (9):
    print("enter",i+1,"elements")
    b= int(input())
    a.append(b)
print(a)
for p in range(3):
    for q in range(3):
        print(a[r],end=' ')
        r=r+1
    print( )