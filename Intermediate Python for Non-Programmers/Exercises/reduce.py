class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def __repr__(self):
        return f"{self.name}: {self.score}"
    
    
    
students = [Student("Joe", 0.46), Student("Amy", 0.72), Student("Mark", 0.88), Student("Zack", 0.99), Student("Jane", 0.79), Student("Sarah", 0.57)]


score_total = 0
for student in students:
    score_total += student.score


from functools import reduce

reduce_total = reduce(lambda total, student: student.score + total, students, 0)

print(round(reduce_total / len(students), 2))
    
    
    