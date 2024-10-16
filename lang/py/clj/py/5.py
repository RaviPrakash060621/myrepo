n=int(input('enter length of list : '))
print(n)
a=[]
for i in range (n):
    b=int(input('enter '+str(i+1)+' element : '))
    # print("enter",i+1,"elements : ")
    # b=int(input())
    a.append(b)
x=int(input('enter number to search : '))

if x in a :
    print(x,' is present at index ',a.index(x))
else:
    print(x,' is not found ')