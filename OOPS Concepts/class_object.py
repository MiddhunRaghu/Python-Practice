class Student:
    def say_hello(self):  
        print("Hi! I am a Student..")


s1 = Student()
s1.say_hello() #python will send like s1.say_hello(s1) , thats why inside class while creating method(function) need to provide "self"

