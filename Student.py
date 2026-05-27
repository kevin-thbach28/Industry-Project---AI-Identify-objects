from User import User, Role

class Student(User):
    def __init__(self, username, password, student_id):
        super().__init__(
            username,
            password,
            Role.STUDENT
        )
        self.student_id = student_id