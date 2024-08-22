class MaxStudents(Exception):
    def __init__(self, message="max students"):
        self.message = message
        super().__init__(self.message)
class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise MaxStudents()
        self.group.add(student)
    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group) if self.group else 'No student in the group.'
        return f'Number: {self.number}\\n {all_students}'
