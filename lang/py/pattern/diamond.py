a = int(input("enter height of half diamond :"))


for i in range(a,0,-1):
        print(" "*(i-1),"*"*(2*(a-i)+1))

        
for i in range(1,a):
        print(" "*i,"*"*(2*(a-i-1)+1))
