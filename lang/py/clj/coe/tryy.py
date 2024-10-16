d1={'a':10,'b':20,'c':50}
print(d1)
d1['c']=30
d1['d']=50
print(d1)

for i in d1:
    print(i,':',d1[i])

d1.pop('a')
del d1['b']

print(d1.items())
print(d1.keys())
print(d1.values())
print(d1.get('c'),'<=>',d1['c'])
l=len(d1)
print(l)
d1.clear()
print(d1)


d2={'e':70,'f':80}
d1.update(d2)
print(d1)

ab=dict([('b1',20),('c1',30),('d1',50)],e1=90)


print(ab)

