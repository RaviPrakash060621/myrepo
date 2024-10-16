#**************************************area of circle**************************************************************#

'''
def circle():
    r=int(input("enter the radius of circle: "))
    area=float(3.14159*r*r)
    print(area,"is area of circle")


circle()

'''

#*************************************name in reverse order**************************************************************#

'''

def rev():
    n1=input('enter your first name : ')
    n2=input('enter your last  name : ')
    n3=n1+n2

    for i in range(len(n3)):
        print(n3[len(n3)-i-1],end=(' '))

rev()

'''

#**********************************commas-seperated no. as list and tuple*****************************************************#


'''

z=input("enter comma sepereted numbers")
z=z+","
l=[]
a=''
for i in range(len(z)):
    
    if z[i]!=',':
        a=a+z[i]
    else:
        l.append(a)
        a=''
        continue
t=tuple(l)
print(l)
print(t)

'''

#**********************************print extension from filename*****************************************************#


'''

a=input('enter file name with extension')
e=''
for i in range(a.find('.')+1,len(a)):
    e=e+a[i]
print('extension of the file is : ',e)


'''



#******************************************n+nn+nnn*****************************************************#

'''

a=int(input('enter an integer n ='))
a1=str(a)+str(a)
a2=str(a)+str(a)+str(a)
a3=a+int(a1)+int(a2)
print ('value of n+nn+nnn = ',a3)

'''



#******************************************sum of 3 numbers*****************************************************#

'''

n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))

avg=(n1+n1+n3)/3

print("average of given numbers is :",avg)
'''


#******************************************count 4 in given list*****************************************************#
'''

l=list(input('enter number for elements in list'))

s=str(l)
print(s.count('4'))

'''




'''                     OR                                   '''



'''  


l=[]
n=int(input('number of elementts in list = ' ))
for i in range(n):
    print(i+1,end='')
    z=int(input(' element of list = '))
    l.append(z)

c=0
for i in range(n):
    a=l[i]
    b=int(a)
    if int(l[i])==4 :
        c=c+1
    else:
        continue
print('count of 4 in list = ',c)


'''