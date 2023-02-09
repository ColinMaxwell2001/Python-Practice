class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    
students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88),
            Student("Zack", 0.99), Student("Jane", 0.79), Student("Sarah", 0.57)]

student_results = []
for student in students:
    
    student_results.append(f"{student.name} Passed") if student.score >= 0.7 else student_results.append(f"{student.name} Failed!")

# create map object, takes list of students and makes a list of student names
map_results = map(lambda student: f"{student.name} Passed") if student.score >= 0.7 else f"{student.name} Failed!"

print(map_results)