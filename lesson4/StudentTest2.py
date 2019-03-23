class Human:
    name = ''
    age = 0
    sex = ''

    def __init__(self, name, age, sex) -> None:
        self.name = name
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return self.name + "," +str(self.age) + "," + self.sex


class Student(Human):
    number = 0
    grade = ''

    def __init__(self, name, age, sex, number, grade) -> None:
        super().__init__(name, age, sex)
        self.number = number
        self.grade = grade

    def __str__(self) -> str:
        return str(self.number) + "," + self.grade + "," + super().__str__()
        #return str(self.number) + "," + self.grade + "," + Human.__str__(self)


student = Student('Vincent', 7, '男', 6, '一年級')
print(student)
