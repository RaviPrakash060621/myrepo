class A:
    a=12
    def displayA(self):
        print(self.a)
    def demo(d):
        print(d.a)
    def sum(r,x,y):
        s=x+y
        print(s)

obj=A()
obj.demo()
obj.displayA()
obj.sum(5,4)
print(obj.a)