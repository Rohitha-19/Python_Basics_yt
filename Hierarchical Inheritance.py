# Parent Class
class Dad:
    def money(self):
        print("Dad's Money")
# Child Class 1
class Son1(Dad):
    pass
# Child Class 2
class Son2(Dad):
    pass
# Child Class 3
class Son3(Dad):
    pass
# Object Creation
s2 = Son2()
# Calling Parent Method
s2.money()

OUTPUT:

Dad's Money
