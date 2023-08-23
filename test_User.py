from classes.User import User
from classes.ListOfUsers import ListOfUsers

def test_creating_a_new_user_in_list():
    user = User('Filipe', 19, '06/03/2004')
    new_list = ListOfUsers()
    result = new_list.insert_user(user)

    assert 'User added in the list !' == result

def test_failing_creating_a_new_user_in_list():
    user = 1
    new_list = ListOfUsers()
    result = new_list.insert_user(user)

    assert 'Not a user, could not add in list !' == result