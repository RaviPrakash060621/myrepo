
# z='welcOm tO kiRa worLd'
# y=z.lower()
# print(y)
# y=z.upper()
# print(y)
# y=z.title()
# print(y)
# y=z.capitalize()
# print(y)


#find function

x="Welcom to kira world"
print(x.find("c"),x.find("r",-1),x.find("l"),x.find("z"),sep=(" --- "))


print(x.index("c"),x.index("r"),sep=(" --- "))


w="welcom123"


print(w.isdigit(),w.isalpha(),w.isalnum(),sep=(" --- "))

w="welcom@#%#&123"


print(w.isdigit(),w.isalpha(),w.isalnum(),sep=(" --- "))



z="welcom to kira world"
y=z.upper()
x=z.lower()
w=z.title()
v=z.capitalize()
print(y,x,w,v,sep=("----"))