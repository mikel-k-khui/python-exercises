class Animal:
  def walk(self):
    print("Walking...")

class Dog(Animal):
  def __init__(self, name, age):
    """Create a dog subclass of animal"""
    self.name = name
    self.age = age

  def __gt__(self, other): #operator overload
    return True if self.age > other.age else False

  def bark(self):
    """Let the dogie bark"""
    print("woof!")

  def walk(self):
    print(f"{self.name} strutting...")
