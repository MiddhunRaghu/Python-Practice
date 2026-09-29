#Single level Inheritence
# class dad:
#     def house(self):
#         print("Red")

# class son (dad):
#     def factory(self):
#         print("White")

#     def house(self): 
#         print("Yellow")


# s =son()
# s.house()
# s.factory()

#Multi Level Inheritence
class grandfather:
    def car(self):
        print("White car")

class dad(grandfather):
    def house(self):
        print("Red")

class son (dad):
    def factory(self):
        print("White")

    def house(self): 
        print("Yellow")


s =son()
s.house()
s.factory()
s.car()
