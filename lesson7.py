class A:
    def __init__(self, name = ""):
        self.name = name

    @classmethod
    def method(cls):
        cls.my_list = []

    @staticmethod
    def method2():
        my_list = []

A.method()
print(A.my_list)

a = A("asdf")
b = A("hjtr")
print(a.my_list)
print(b.my_list)
print(A.my_list)
print(a.my_list is b.my_list is A.my_list)