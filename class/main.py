class Hello:
    count =0
    def __init__(self, name):
        self.name = name

    def sayhello(self):
        return "Hello world " + self.name

    @staticmethod
    def staticmethod():
        return "static method"

    @classmethod
    def classmethod(cls):
        return cls.count


obj = Hello("Rajesh")
print(obj.sayhello())
print(Hello.staticmethod())
print(Hello.classmethod())
