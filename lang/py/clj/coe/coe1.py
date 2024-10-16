# s=ord("+")
# print(s)
# d=chr(69)
# print(d)


# for a in range(9,12,2):
#     print(a)


a="hello to kira world"
print(a[9:])
print(a[::2])
print(a[-1::-1])



# i=len(a)

# for j in range(1,i+1):
#     print(a[-j])



#cal
#with elif
z=int(input("enter 1st no."))
y=int(input("enter 2st no."))
x=input('''Select operation 
 A. + : addition
 B. - : subtraction 
 C. * : multiplication 
 D. / : division
 enter your choice :''')
if x=='A':
    print(z+y)
elif x=='B':
    print(z-y)
elif x=='C':
    print(z*y)
elif x=='D':
    print(z/y)
else:
    print('invalid input')

#cal. with if else
z=int(input("enter 1st no."))
y=int(input("enter 2st no."))
x=input('''Select operation 
 A. + : addition
 B. - : subtraction 
 C. * : multiplication 
 D. / : division
 enter your choice :''')
if x=='A':
    print(z+y)
else:
    if x=='B':
        print(z-y)
    else:
        if x=='C':
            print(z*y)
        else:
            if x=='D':
                print(z/y)
            else:
                print('invalid input')
    
    
# percentage to gread
z=int(input("enter your percent to know your grade"))
if z>98:
    print('A grade : excellent chlo ab blackboard saf kro ')
elif (z<=98)  and (z>95): 
    print('B grade : good ,still study more')
elif (z<=95)  and (z>90):
    print('c grade : average ,work hard')
elif (z<=90)  and (z>80):
    print('D grade : below average , padh liya kr kavi')
elif (z<=75):
    print('F grade :failureeee , paisa barbad ###')
