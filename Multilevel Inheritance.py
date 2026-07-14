# Grandparent Class
class Grandpa:
    def phone(self):
        print("Grandpa's Phone")
# Parent Class
class Dad(Grandpa):
    def money(self):
        print("Dad's Money")
# Child Class
class Son(Dad):
    def laptop(self):
        print("Son's Laptop")
# Object of Son
ram = Son()

ram.laptop()
ram.money()
ram.phone()

# Object of Dad
d1 = Dad()
d1.phone()

OUTPUT:

Son's Laptop
Dad's Money
Grandpa's Phone
Grandpa's Phone
