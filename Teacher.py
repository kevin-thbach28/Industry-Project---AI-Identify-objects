from User import User, Role

class Teacher(User):
    def __init__(self, username, password, teacher_id):
        super().__init__(
            username,
            password,
            Role.TEACHER
        )
        self.teacher_id = teacher_id