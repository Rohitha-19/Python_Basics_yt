class Laptop:
    # Class Variable
    charger_type = "C TYPE"

    # Constructor
    def __init__(self):
        # Instance Variables
        self.brand = ""
        self.price = 0

    # Instance Method
    def setPrice(self, price):
        self.price = price

    # Instance Method
    def getPrice(self):
        print("Price:", self.price)

    # Class Method
    @classmethod
    def changeChargerType(cls):
        cls.charger_type = "B TYPE"
        print("Charger type changed to B TYPE")

    # Static Method
    @staticmethod
    def info():
        print("This is Laptop class")
# Object Creation
hp = Laptop()

# Calling Instance Method
hp.setPrice(20000)
hp.getPrice()

# Calling Class Method
Laptop.changeChargerType()

# Accessing Class Variable
print("Charger Type:", Laptop.charger_type)

# Calling Static Method
hp.info()




OUTPUT:

Price: 20000
Charger type changed to B TYPE
Charger Type: B TYPE
This is Laptop class
