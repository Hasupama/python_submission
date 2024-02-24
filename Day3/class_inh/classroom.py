
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    def print_Person(self):
        print(self.firstname + ' ' + self.lastname)

name = Person("Hasupama", "Jayasinghe")
name.print_Person()



class Student(Person):
    def __init__(self, firstname, lastname, area):
        super().__init__(firstname, lastname)
        self.area = area
        
    def print_NameSubject(self):
        print(self.firstname + ' ' + self.lastname + ', ' + self.area)
        
 
name_st = Student("Benedikt", "Daurer", "physics")
name_st.print_NameSubject()
 

class Teacher(Person):
    def __init__(self, firstname, lastname, course):
        super().__init__(firstname, lastname)
        self.course = course
        
    def print_TeacherCourse(self):
        print(self.firstname + ' ' + self.lastname + ', ' + self.course)
        
name_te = Teacher("Filipe", "Maia", "python 2024")
name_te.print_TeacherCourse()
