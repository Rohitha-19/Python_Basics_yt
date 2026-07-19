class company():
  def __init__(self):
    self.companyName="Google"
c1=company()
print(c1.companyName)
#Output: Google
---
class company():
  def __init__(self):
    self.companyName="Google"
c1=company()  #this is called objects, we create object for this class.
c1.companyName="Goooogle"   #anyone unknown person can change the name of anything, in this the google can be change into goooogle by unknown person, to prevent this we can use "ACCESS MODIFIERS"
print(c1.companyName)
#Output: Goooogle
---

__ - private access modifier symbol
_  - protector access modifier symbol

class company():
  def __init__(self):
    self.__companyName="Google"
    
  def companyName(self):
    print(self.__companyName) #called inside the class, so the output will be shown. this is private access modifier. and this is called "Encapsulation,bcz we hiding some info, using private access modifier"
    
c1=company()
c1.companyName()
#Output: Google
