Hybrid Inheritance (a combination of multiple & hierarchical inheritance)

# Parent Class 1
class Dad:
    def money(self):
        print("Dad's Money")
# Parent Class 2
class Land:
    def important(self):
        print("Important Land")
# Child Class (Multiple Inheritance)
class Son1(Dad, Land):
    pass
# Child Class (Hierarchical Inheritance)
class Son2(Dad):
    pass
# Child Class (Hierarchical Inheritance)
class Son3(Dad):
    pass
# Object Creation
s2 = Son2()
# Calling Parent Method
s2.money()
# Object of Son1
s1 = Son1()
s1.money()
s1.important()

OUTPUT:

Dad's Money
Dad's Money
Important Land
