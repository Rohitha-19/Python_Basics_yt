# Parent Class
class Dad:
    def phone(self):
        print("Dad's Phone")
# Child Class
class Son(Dad):
    def laptop(self):
        print("Son's Laptop")
# Object Creation
ram = Son()

# Calling Parent Class Method
ram.phone()

# Calling Child Class Method
ram.laptop()
