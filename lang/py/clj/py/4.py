def gcd(n1,n2):
    if n1==n2:
        print("gcd = ",n1)
    
    elif n1<n2 :
        for i in range(n1,0,-1):
            if n1%i==0 and n2%i==0 :
                print("gcd = ",i)
                break
            
    else:
        for i in range(n2,0,-1):
            if n2%i==0 and n1%i==0 :
                print("gcd = ",i)
                break

            
gcd(15,30)