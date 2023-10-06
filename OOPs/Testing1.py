class A:
    def __init__(self) -> None:
        print("A")
        self.a = 1
    def cf(self):
        return 'a'

class B:
    def __init__(self, val) -> None:
        print("B")
        self.b = val
    def cf(self):
        return 'b'

class C(A, B):
    def __init__(self, val) -> None:
        acls, bcls = C.__bases__
        acls.__init__(self)
        bcls.__init__(self, val)
        print("C")
        self.c = 'c'
        self._c = 'c'
        self.__c = 'c'

    def cf(self):
        return super().cf()

c = C(100)
# print(c.cf())
print(c.b)