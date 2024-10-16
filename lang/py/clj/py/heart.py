n=int(input("enter even no "))
N=6+int(n/2-3)

for i in range(N):
        for j in range(n+1):
                
                if (i==0 and j%(n/2)!=0) or (i==1 and j%(n/2)==0) or (i-j==2) or (i+j==n+2):
                         print("*",end=" ")
                else:
                        print(" ",end=" ")
                
        print()
