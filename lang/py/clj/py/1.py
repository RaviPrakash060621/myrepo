'''

def rev():
    a=input('enter  string : ')
    print(a[-1::-1])

    

a='welcome to python class'
def count(n):
    
    print(a.count(n))
count('a')

'''

#a=input('enter string')

a='welcome to python class'
l=list(a)
print(l)
n=len(l)
print(n)
for i in range(n):
    m=['a','e','i','o','u','A',]
    if l[i]=="a" or l[i]=="e" or l[i]=="i" or l[i]=="o" or l[i]=="u":
        print(l[i],end="")
        del l[i]
        l.insert(i,'w')
    else:
        continue
b=str(l)
print(b)
 