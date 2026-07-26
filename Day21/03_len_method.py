# __len__ Method

class Classroom:

    def __init__(self, students):
        self.students = students

    def __len__(self):
        return len(self.students)

classroom = Classroom(["Ridhima", "Rahul", "Anjali"])

print(len(classroom))
