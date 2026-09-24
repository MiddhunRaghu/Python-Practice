class StudentDetails:
    def __init__(self,fname,fage):
        self.name = fname
        self.age = fage

    def fetchdetails(self):
        print(f"Name : {self.name} , Age:  {self.age}")

s1 = StudentDetails("Middhun" , 25)
s2 = StudentDetails("Kishore" , 26)
s1.fetchdetails()
s2.fetchdetails()

