class Temp():
    def normal(self):
        print("normal")

    @staticmethod
    def static():
        Temp.classMethod()
        print("static")

    @classmethod
    def classMethod(cls):
        print("class method")

Temp.static()