'''
a='welcom {} to {} my world'.format('you',1)

print(a)

a='welcom {0} to {1} my world'.format('you',1)

print(a)

a='welcom {1} to {0} my world'.format('you',1)

print(a)

a='welcom {a} to {b} my world'.format(a='aa',b=12)

print(a)

a='welcom {b} to {a} my world'.format(b=22,a='ab')

print(a)

a='welcom {a:10} to {b} my world'.format(a='abcd',b=0)

print(a)

a='welcom {a:^10} to {b} my world'.format(a='abcd',b=0)

print(a)

a='welcom {a:<10} to {b} my world'.format(a='abcd',b=0)

print(a)

a='welcom {a:>10} to {b} my world'.format(a='abcd',b=0)

print(a)

'''


'''
a=[10,20,30,40,[40,50,60],'hello']


print(a[1:3])
print(a[-1])
print(a[4][2])
print(a[::-1])
print(a[1::-1])
print(a[-1::-1])



for i in a:
    print(i)
t=len(a)

for i in range(t):
    print(a[i])

    '''

'''
a=[10,20,30,40,[40,50,60],'hello']

#function of list
#delet fun
del a[0]
print(a)

print(a.pop(2))
print(a)

r=a.remove(30)

print(a)

print(a.pop())

print(a)

'''
#insert fn

'''
a=[10,20,30,40,[40,50,60],'hello']

a[0]=5
print(a)
m=[70,80,90]
a.insert(1,15)
print(a)
a.append('welcom')
print(a)
a.append(m)
print(a)
a.extend(m)
print(a)

'''

for i in range(5):
    print('*'*(i+1),' '*(5-i+1))



for i in range(4):
    print('*'*(4-i),' '*(i))