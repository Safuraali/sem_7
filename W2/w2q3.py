class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def get_details(self):
        return f"Name: {self.name}, ID: {self.student_id}"


class GraduateStudent(Student):
    def __init__(self, name, student_id, thesis_topic):
        super().__init__(name, student_id)
        self.thesis_topic = thesis_topic

    def get_details(self):
        return f"Name: {self.name}, ID: {self.student_id}, Thesis: {self.thesis_topic}"


student1 = Student("Rahul", "S101")
graduate_student1 = GraduateStudent(
    "Safura",
    "G101",
    "Artificial Intelligence and Machine Learning"
)

print(student1.get_details())
print(graduate_student1.get_details())
