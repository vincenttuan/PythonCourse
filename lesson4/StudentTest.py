class Human:
    name = ''
    age = 0
    sex = ''

    def __str__(self) -> str:
        return self.name + "," +str(self.age) + "," + self.sex


class Student(Human):
    number = 0
    grade = ''

    def __str__(self) -> str:
        return str(self.number) + "," + self.grade + "," + super().__str__()
        #return str(self.number) + "," + self.grade + "," + Human.__str__(self)


student = Student()
student.name = 'Vincent'
student.age = 7
student.sex = '男'
student.number = 6
student.grade = '一年級'

print(student.name)
print(student.age)
print(student.sex)
print(student.number)
print(student.grade)

print(student)
