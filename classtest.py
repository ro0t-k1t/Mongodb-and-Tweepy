__author__ = 'ronanpiercehiggins'

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self, other_name):
    return "Hi {0}, my other name is {1}".format(self.name, other_name,)



test = Person("Ronan Higgins")

print test.greet("Higgins")





