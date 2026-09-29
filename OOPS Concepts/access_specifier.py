class parent:
    def __init__(self):
        # Public: accessible from this class, subclasses, and outside code.
        self.public_var = "I am Public"
        # Protected: intended for this class and subclasses; Python does not
        # strictly prevent access from outside the class.
        self._protected_var = "I am Protected"
        # Private: name-mangled by Python, so direct access from subclasses
        # and unrelated classes using __private_var raises AttributeError.
        self.__private_var = "I am Private"

    def access_from_same_class(self):
        # The defining class can access public, protected, and private members.
        print("Inside Parent Class")
        print("Public : ",self.public_var)
        print("Protected : ",self._protected_var)
        print("Private : ",self.__private_var)

class child (parent):
    def access_from_sub_class(self):
        print("Inside Child Class")
        # A subclass can access public and protected attributes.
        print("Public : ",self.public_var)
        print("Protected : ",self._protected_var)
        try:
            # This name is mangled as _child__private_var, not the parent's
            # _parent__private_var, so direct private access fails.
            print("Private : ",self.__private_var)
        except AttributeError:
            print ("Private : ❌ cannot access (AttributeError)")

class stranger:
    def access_from_another_class(self, obj):
        print("Inside a Stranger Class")
        print("Inside Child Class")
        # Public attributes are available through an object from anywhere.
        print("Public : ",obj.public_var)
        # Protected attributes are technically accessible, but the underscore
        # convention says they are intended for internal/subclass use.
        print("Protected : ",obj._protected_var)
        try:
            # An unrelated class cannot access the private attribute directly.
            print("Private : ",obj.__private_var)
        except AttributeError:
            print ("Private : ❌ cannot access (AttributeError)")


p = parent()
c = child()
s = stranger()

print("\n ➜ Access from Same Class")
p.access_from_same_class()

print("\n ➜ Access from Child Class")
c.access_from_sub_class()

print("\n ➜ Access from another Class")
s.access_from_another_class(p)