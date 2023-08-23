from classes.User import User
class ListOfUsers:

    def __init__(self) -> None:
        self.list = []

    def insert_user(self, user):
        if not isinstance(user, User):
            return 'Not a user, could not add in list !'
        self.list.append(user)
        return "User added in the list !"