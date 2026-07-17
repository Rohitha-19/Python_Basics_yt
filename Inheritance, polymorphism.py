class shape():
  def area(self):
    return 0
class rectangle(shape):
  def area(self):
    l=10
    b=20
    print(l*b)
r1=rectangle()
r1.area()

OUTPUT: 200
---

class Person():
  def__init__(self,name):
    self.name=name
class student(Person):
  def__init__(self,name,grade):
  super().__init__(name)
    self.grade=grade
  def display(self):
    print(self.name,self.grade)
s1=student("Rhi", "O")
s1.display()
  
