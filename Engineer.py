from User import User, Role

class Engineer(User):
    def __init__(self, username, password):
        super().__init__(
            username,
            password,
            Role.ENGINEER
        )