# Polymorphism in Python means the same method name can behave differently
# depending on the object calling it.
# Here, the child class overrides the parent class method house().

class dad:
    def house(self):
        print("Red")

class son(dad):
    def factory(self):
        print("White")

    # This method overrides the parent class method with the same name.
    def house(self):
        print("Yellow")

# s is an object of class son, so the child version of house() is used.
# This is an example of polymorphism: same method name, different behavior.
s = son()
s.house()
s.factory()
