class student:
    name="Saurbh"
    age =20
    roll_no=210200111013
    def info(self):
        print(f"Name of student is {self.name} \nAge of the Student is {self.age}\nRoll No. of the student is {self.roll_no}")


a=student()
a.name="Nishant Gupta"
a.age=16
a.roll_no=1

b=student()
b.name="Rahul Sharma"
b.age=17
b.roll_no=2

c=student()
c.name="Anshu"
c.age=16
c.roll_no=3

a.info()
b.info()
c.info()