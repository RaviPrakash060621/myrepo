'''
def gcd(n1,n2):

    if n1<n2 :
        for i in range(n1,0,-1):
            if n1%i==0 and n2%i==0 :
                print(i)
                break
            
    else:
        for i in range(n2,0,-1):
            if n2%i==0 and n1%i==0 :
                print(i)
                break
gcd(30,15)

'''
'''

for i in range(5):
    print("*"*(i+1)," "*(5-i)) 

for i in range(5):
    print(" "*(5-i-1),"*"*(i+1))

for i in range(5,0,-1):
        print(" "*(i-1),"*"*(2*(5-i)+1)) 


a=65
for i in range(5):
    for j in range(i+1):
        print(chr(a),end=" ")
        a=a+1

    print()
'''


'''

n1=int(input("enter 1st number"))
n2=int(input("enter 2nd number"))
n3=int(input("enter 3rd number"))

avg=(n1+n1+n3)/3

print("average of given numbers is :",avg)

'''

'''

y=int(input('enter year :'))
if y%4==0 or y%100==0 or y%400==0 :
    print (y,'is a leap year')
else:
    print(y,'  is not a leap year')

'''
'''

n=int(input('enter number :'))
for i in range (1,11):
    print(n,'x',i,'=',n*i)

'''
