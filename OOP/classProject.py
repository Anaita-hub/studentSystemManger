class Student:
    def __init__(self,name,age,major):
        self.name=name
        self.age=age
        self.major =major
        self.grades=[]

    def add_grade(self,grade):
        if 0<=grade<=100:  
            self.grades.append(grade)
        else:
            print("Wrong number")

    def calculate_gpa(self):
        if self.grades:
            return sum(self.grades)/len(self.grades)
        else:
            return 0
    
    def display_inf(self):
        gpa=self.calculate_gpa()
        print(f"Name:{self.name}, Age:{self.age},major:{self.major},gpa:{gpa:.2f}")
        

#objects
st1=Student("Fatima",20, "BCS")
st2=Student("Sana",19,"BCS")
st3=Student("Sayeda",18,"BCS")


#st1-add number
st1.add_grade(200)
st1.add_grade(190)
st1.add_grade(-60)
st1.add_grade(99)

#st2 -add number
st2.add_grade(300)
st2.add_grade(60)
st2.add_grade(89)
st2.add_grade(90)

#st3 - add number
st3.add_grade(700)
st3.add_grade(49)
st3.add_grade(99)
st3.add_grade(87)

st1.display_inf()
st2.display_inf()
st3.display_inf()



