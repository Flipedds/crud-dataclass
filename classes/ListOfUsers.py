from classes.User import User
class ListOfUsers:

    def __init__(self) -> None:
        self.list = []

    def insert_user(self, user):
        if not isinstance(user, User):
            return 'Not a user, could not add in list !'
        self.list.append(user)
        return "User added in the list !"
    
    def remove_user(self, index):
        pointer = self.list.index(self.list[-1])
        if index > pointer:
            return "User don't exists"
        self.list.pop(index)
        return f'User {index} removed !'