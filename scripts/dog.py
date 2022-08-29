class Animal:
  def walk(self):
    print("Walking...")

class Dog(Animal):
  def __init__(self, name, breed):
    """Create a dog subclass of animal"""
    self.name = name
    self.breed = breed

  def bark(self):
    """Let the dogie bark"""
    print("woof!")

  def walk(self):
    print("Strutting...")
