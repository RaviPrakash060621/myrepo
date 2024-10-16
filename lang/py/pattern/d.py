'''               diamond             '''
# n=int(input("enter length of diamond "))
# for i in range(n):
#     print(" "*(n-1-i),"*"*(2*i +1))

# for i in range(n-1):
#     print(" "*(i+1),"*"*((2*(n-2-i))+1))


 
'''                          hollow diamond                                 '''

n=int(input("enter length of diamond "))
for i in range(n):
    if i==0 :
        print(" "*(n-1)," *")
    else:
        print(" "*(n-1-i),"*"," "*(2*(i-1)+1),"*")


for i in range(n-1):
    if i==n-2 :
        print(" "*(n-1)," *")
    else:
        print(" "*(i+1),"*"," "*(2*(n-3-i)+1),"*")





'''                          butterfly                                     '''

