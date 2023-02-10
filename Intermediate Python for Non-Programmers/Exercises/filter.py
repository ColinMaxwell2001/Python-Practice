class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name}: {self.score}"

#end of Student Class


students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88),
            Student("Zack", 0.99), Student("Jane", 0.79), Student("Sarah", 0.57)]

failing_students = []
for student in students:
    if student.score < 0.7:
        failing_students.append(student)

filter_list = list(filter(lambda student: student.score < 0.7, students))


print(filter_list)