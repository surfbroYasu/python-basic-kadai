class Human:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printinfo(self):
    print(self.name + " " + str(self.age))


# testing: instances/methods
    
john = Human("John", 26)
john.printinfo()

jacob = Human("Jacob", 35)
jacob.printinfo()