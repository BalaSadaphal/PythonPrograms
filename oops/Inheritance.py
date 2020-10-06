class A:
    def __init__(self):
        print("A's constructor")

    def feature1(self):
        print("in A feature1")

    def feature2(self):
        print("in feature2")


class B:
    def __init__(self):
        print("B's constructor")

    def feature1(self):
        print("in B feature1")

    def feature4(self):
        print("in feature4")


class C(B, A):
    def feature4(self):
        self.feature1()
        print("in feature4")

    def feature4(self, p1):
        print(f"in feature4, {p1}")


c1 = C()
c1.feature4(1)
c1.feature4('hello there')
