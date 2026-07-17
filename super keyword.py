class A:
    def __init__(self):
        print("A")
    def display(self):
        print("You are in class A")

class B(A):

    def __init__(self):
        super().__init__()
        print("B")

    def display(self):
        print("You are in class B")
# Class C
class C(B):

    def __init__(self):
        super().__init__()
        print("C")

    def display(self):
        print("You are in class C")

obj = C()

OUTPUT:

A
B
C
