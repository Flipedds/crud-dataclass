class ListOfUsers:

    def __init__(self) -> None:
        self.list = []

    def insert_user(self, user):
        self.list.append(user)
        return "User added in the list !"