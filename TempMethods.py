class MyObj():
    def __init__(self):
        self.x = 100

class Temp():
    def m1(self):
        l = [1,2,3]
        m = MyObj()
        self.m2(m)

    def m2(self, m):
        print(m.x)

c = Temp()
c.m1()