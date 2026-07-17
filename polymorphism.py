class Animal():  #class
  def sound(self):
    print("Animal makes sound")

class Dog(Animal): 
  def sound(self):       #method overriding
    print("Dog Barks")

class Bird(Animal): #inherites
  def sound(self):    #method overriding
    print("Birds Sing")

a1=Animal()
a1.sound()

b1=Dog()
b1.sound()

c1=Bird()
c1.sound()
