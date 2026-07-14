# Parent Class 1
class Dad:
    def phone(self):
        print("Dad's Phone")
# Parent Class 2
class Mom:
    def sweet(self):
        print("Mom's Sweet")
# Child Class
class Son(Dad, Mom):
    def laptop(self):
        print("Son's Laptop")
# Object Creation
ram = Son()
# Calling Methods
ram.phone()
ram.sweet()
ram.laptop()


OUTPUT:

Dad's Phone
Mom's Sweet
Son's Laptop
